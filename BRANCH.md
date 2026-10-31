# Branch `pytest-none`

A small, correct calculator module with no tests yet.
Starting point for writing the first pytest tests.

- Parent branch: `main`
- Used in: Video 2 - pytest basics

## Commands

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m pytest -q --no-header
```

## Expected output

pytest finds nothing to run and exits with code 5 (pytest's "no tests collected" code):

```text
no tests ran in 0.02s
```

Timings (`in 0.35s`) and object addresses vary from run to run.
