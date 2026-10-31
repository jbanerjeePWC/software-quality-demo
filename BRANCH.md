# Branch `lint-bad`

Starting from app-mini, docstrings are removed and the except clause is made bare and
falls through. Pylint reports exactly eight messages.

- Parent branch: `app-mini`
- Used in: Video 3 - Linting with pylint

## Commands

```powershell
pip install -r requirements-dev.txt
python -m pylint app.py model.py
```

## Expected output

Exit code 28 (pylint's bit flags: 4 warning + 8 refactor + 16 convention).

```text
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:4: W0702: No exception type(s) specified (bare-except)
app.py:14:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module model
model.py:1:0: C0114: Missing module docstring (missing-module-docstring)
model.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
model.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)

-------------------------------------------------------------------
Your code has been rated at 7.84/10 (previous run: 10.00/10, -2.16)
```

The `(previous run: ...)` part of pylint's score line depends on your local pylint
history and will differ; the messages and the score itself are fixed.

| Message | Count | Where |
| --- | --- | --- |
| C0114 missing-module-docstring | 2 | app.py, model.py |
| C0116 missing-function-docstring | 4 | home, prediction, preprocess_img, predict_result |
| W0702 bare-except | 1 | prediction |
| R1710 inconsistent-return-statements | 1 | prediction (the except branch only prints) |

Score: 10 - 10 x (8 messages / 37 statements) = 7.84.
