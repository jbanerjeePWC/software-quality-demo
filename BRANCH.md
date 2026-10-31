# Branch `app-mini`

A tiny Flask digit-recognition app with the same structure as the student assignment,
using a fake, deterministic numpy model (no TensorFlow). Pylint 10.00/10.

- Parent branch: `main`
- Used in: Base branch for videos 3-6 (pylint, pre-commit, better tests, CI)

## Layout

| Path | Purpose |
| --- | --- |
| `app.py` | Flask app: `GET /` (`home`) and `POST /prediction` (`prediction`) |
| `model.py` | `FakeDigitModel`, `preprocess_img`, `predict_result` |
| `templates/` | `index.html` (upload form), `result.html` (always has the heading "Prediction") |
| `static/style.css` | styling |
| `test_images/` | `digit_2.png`, `digit_7.png` (uniform gray, made by `tools/make_test_images.py`) |
| `.pylintrc` | py-version 3.10, max line length 100, snake_case names, fail-under 10 |

The fake model predicts `min(9, int(mean_brightness * 10))`. The test images have gray levels
`round(digit * 25.5 + 13)`, i.e. 64 and 192.

Note: `prediction()` catches only `(KeyError, OSError, ValueError)`. `RuntimeError` is
deliberately not caught (see the `ci-test-fail` branch).

## Commands

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m pylint app.py model.py
python -m flask --app app.py run --debugger --port 9000
```

Then open http://127.0.0.1:9000/ and upload `test_images/digit_2.png` or `digit_7.png`.

## Expected output

`python -m pylint app.py model.py` (exit code 0):

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

The `(previous run: ...)` part of pylint's score line depends on your local pylint
history and will differ; the messages and the score itself are fixed.

Server start:

```text
 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:9000
Press CTRL+C to quit
```

Route checks (Flask test client; the same results were seen with `curl` against the running
server):

```text
predict_result(preprocess_img('test_images/digit_2.png')) -> 2
predict_result(preprocess_img('test_images/digit_7.png')) -> 7
GET / -> 200 []
POST /prediction digit_2.png -> 200 ['Predicted digit: 2']
POST /prediction digit_7.png -> 200 ['Predicted digit: 7']
POST /prediction (no file field) -> 200 ['Could not process the image']
POST /prediction (empty filename) -> 200 ['No file selected']
POST /prediction (text file) -> 200 ['Could not process the image']
```

`python tools/make_test_images.py` regenerates identical PNGs:

```text
wrote digit_2.png (gray level 64)
wrote digit_7.png (gray level 192)
```
