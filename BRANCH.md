# Branch `tests-improved`

Keeps the old tests and adds improved `_new` versions with a shared conftest.py, real
in-memory PNGs, precise assertions and mocks patched where they are used.

- Parent branch: `tests-weak`
- Used in: Video 5 - Writing better tests

## Weak vs improved

| Aspect | Weak (`*_old.py`) | Improved (`*_new.py`) |
| --- | --- | --- |
| Setup | new test client in every test | `client` fixture in conftest.py |
| Test data | text bytes named `large.png` | real PNGs built with Pillow (`make_png_bytes`) |
| Assertions | `b"Prediction" in body` (always true) | exact text: `Predicted digit: 2`, error message, status code |
| Isolation | runs the whole stack | `unittest.mock.patch("app.preprocess_img")` / `("app.predict_result")` |
| Mock checks | none | `assert_called_once()` and the batch passed through |
| Error paths | not really tested | missing field, empty filename, invalid bytes, missing path |
| Model output | `is not None` | shape, dtype, value range, argmax, end-to-end digits 2 and 7 |
| File paths | relative to the current directory | relative to the test file |

## Commands

```powershell
pip install -r requirements-dev.txt
python -m pytest -q --no-header
python -m pytest -v --no-header
python -m pylint app.py model.py
```

## Expected output

`python -m pytest -q --no-header` (exit code 0; 5 old + 12 new tests):

```text
.................                                                        [100%]
17 passed in 0.35s
```

`python -m pytest -v --no-header`:

```text
============================= test session starts =============================
collecting ... collected 17 items

test_app_new.py::test_home_page_returns_upload_form PASSED               [  5%]
test_app_new.py::test_valid_large_image_upload_new PASSED                [ 11%]
test_app_new.py::test_missing_file_field_returns_controlled_error PASSED [ 17%]
test_app_new.py::test_empty_filename_is_handled PASSED                   [ 23%]
test_app_new.py::test_invalid_image_bytes_return_controlled_error PASSED [ 29%]
test_app_old.py::test_home_page PASSED                                   [ 35%]
test_app_old.py::test_prediction_upload PASSED                           [ 41%]
test_app_old.py::test_missing_file PASSED                                [ 47%]
test_model_new.py::test_preprocess_img_shape_dtype_and_range PASSED      [ 52%]
test_model_new.py::test_preprocess_resizes_small_and_large_images[10-10] PASSED [ 58%]
test_model_new.py::test_preprocess_resizes_small_and_large_images[2000-1500] PASSED [ 64%]
test_model_new.py::test_predict_result_returns_index_of_highest_score PASSED [ 70%]
test_model_new.py::test_preprocess_missing_path_raises_file_not_found PASSED [ 76%]
test_model_new.py::test_predict_digit_2_image_end_to_end PASSED          [ 82%]
test_model_new.py::test_predict_digit_7_image_end_to_end PASSED          [ 88%]
test_model_old.py::test_preprocess_img PASSED                            [ 94%]
test_model_old.py::test_predict_result PASSED                            [100%]

============================= 17 passed in 0.32s ==============================
```

Pylint (exit code 0):

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Timings (`in 0.35s`) and object addresses vary from run to run. The `(previous run: ...)` part of pylint's score line depends on your local pylint
history and will differ; the messages and the score itself are fixed.
