# Branch `tests-weak`

Beginner-style tests: no fixtures, no mocks, weak assertions. All pass, but some pass
for the wrong reason.

- Parent branch: `app-mini`
- Used in: Video 5 - Writing better tests

## The weak spots (on purpose)

- `test_prediction_upload` uploads text bytes named `large.png` and only checks that
  `b"Prediction"` is in the page. The upload is not an image, so the app shows its error
  message, but `result.html` always contains the heading "Prediction". The test passes for
  the wrong reason.
- `test_missing_file` has the same problem.
- `test_model_old.py` only checks `is not None` and uses a path relative to the current
  directory.

## Commands

```powershell
pip install -r requirements-dev.txt
python -m pytest -v --no-header
python -m pylint app.py model.py
```

## Expected output

`python -m pytest -q --no-header` (exit code 0):

```text
.....                                                                    [100%]
5 passed in 0.68s
```

`python -m pytest -v --no-header`:

```text
============================= test session starts =============================
collecting ... collected 5 items

test_app_old.py::test_home_page PASSED                                   [ 20%]
test_app_old.py::test_prediction_upload PASSED                           [ 40%]
test_app_old.py::test_missing_file PASSED                                [ 60%]
test_model_old.py::test_preprocess_img PASSED                            [ 80%]
test_model_old.py::test_predict_result PASSED                            [100%]

============================== 5 passed in 0.63s ==============================
```

Pylint (exit code 0):

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Timings (`in 0.35s`) and object addresses vary from run to run. The `(previous run: ...)` part of pylint's score line depends on your local pylint
history and will differ; the messages and the score itself are fixed.
