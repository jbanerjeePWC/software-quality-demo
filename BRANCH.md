# Branch `ci-lint-fail`

Removes the module docstring from app.py only. Pylint fails, so CI stops at the
Run Pylint step and the Run tests step is skipped.

- Parent branch: `ci-pass`
- Used in: Video 6 - Continuous integration with GitHub Actions

## Commands

```powershell
python -m pip install -r requirements.txt
python -m pip install pylint pytest
python -m pylint app.py model.py
python -m pytest -q --no-header
```

## Expected output

Pylint (exit code 16):

```text
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-------------------------------------------------------------------
Your code has been rated at 9.73/10 (previous run: 10.00/10, -0.27)
```

Pytest still passes locally (exit code 0):

```text
.................                                                        [100%]
17 passed in 0.44s
```

Expected in GitHub Actions: the run fails at **Run Pylint**; **Run tests** is skipped.
