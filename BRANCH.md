# Branch `ci-test-fail`

Adds a regression test: when the model raises RuntimeError the app should still answer
with HTTP 200 and an error message. app.py does not catch RuntimeError, so it fails.

- Parent branch: `ci-pass`
- Used in: Video 6 - Continuous integration with GitHub Actions

The test sets `PROPAGATE_EXCEPTIONS = False` (with `monkeypatch`, so it is undone afterwards).
In TESTING mode Flask would otherwise re-raise the RuntimeError inside the test instead of
returning the HTTP 500 a real user would get.

## Commands

```powershell
python -m pip install -r requirements.txt
python -m pip install pylint pytest
python -m pylint app.py model.py
python -m pytest -q --no-header
```

## Expected output

Pylint passes (exit code 0):

```text
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.73/10, +0.27)
```

Pytest fails (exit code 1). Excerpt:

```text
______________________ test_prediction_runtime_error_new ______________________

client = <FlaskClient <Flask 'app'>>
make_png_bytes = <function make_png_bytes.<locals>._make_png_bytes at 0x0000018F5AA7F250>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x0000018F5AA85990>

    def test_prediction_runtime_error_new(client, make_png_bytes, monkeypatch):
        # Behave like production: in TESTING mode Flask re-raises unhandled exceptions
        # inside the test; with this off, they become an HTTP 500 response instead.
        monkeypatch.setitem(client.application.config, "PROPAGATE_EXCEPTIONS", False)
        fake_batch = np.zeros((1, 28, 28, 1), dtype=np.float32)
        failure = RuntimeError("simulated model runtime failure")
        data = {"file": (io.BytesIO(make_png_bytes(64, 64)), "digit.png")}

        with (
            patch("app.preprocess_img", return_value=fake_batch),
            patch("app.predict_result", side_effect=failure),
        ):
            response = client.post("/prediction", data=data, content_type="multipart/form-data")

>       assert response.status_code == 200
E       assert 500 == 200
E        +  where 500 = <WrapperTestResponse streamed [500 INTERNAL SERVER ERROR]>.status_code

test_integration_sad_new.py:22: AssertionError
...
RuntimeError: simulated model runtime failure
=========================== short test summary info ===========================
FAILED test_integration_sad_new.py::test_prediction_runtime_error_new - asser...
1 failed, 17 passed in 0.68s
```

Expected in GitHub Actions: **Run Pylint** passes, **Run tests** fails.

Timings (`in 0.35s`) and object addresses vary from run to run.
