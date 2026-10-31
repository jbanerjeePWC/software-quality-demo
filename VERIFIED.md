# Verified results

Every branch was cloned into a scratch folder and checked with fresh virtual environments
created outside the repository. Python 3.10.22 on Windows 11.

- App branches: `requirements-dev.txt` (Flask 2.2.2, Werkzeug 2.2.2, Pillow 12.3.0,
  numpy 2.2.6, pylint 4.1.3, pytest 9.2.0, pre-commit 4.6.2).
- `ci-*` branches: a CI-like venv with `requirements.txt` plus unpinned `pylint pytest`
  (resolved to pylint 4.1.3 and pytest 9.2.0).
- pytest branches: `requirements-dev.txt` (pytest 9.2.0).
- Every tracked text file uses LF line endings, has no BOM, and compiles under Python 3.10.

| Branch | Parent | Commits ahead | Verified command | Exit code | Key output |
| --- | --- | --- | --- | --- | --- |
| `env-demo` | `main` | 1 | `python whichpython.py (venv)` | 0 | shows the venv executable and prefix |
|  |  |  | `python hello_requests.py (before install)` | 1 | ModuleNotFoundError: No module named 'requests' |
|  |  |  | `pip install -r requirements.txt` | 0 | installed |
|  |  |  | `python hello_requests.py (after install)` | 0 | requests version: 2.32.3 |
|  |  |  | `pip install -r requirements-unpinned.txt` | 0 | installed Werkzeug 3.1.9 |
|  |  |  | `python import_flask.py (unpinned)` | 1 | ImportError: cannot import name 'url_quote' from 'werkzeug.urls' |
|  |  |  | `pip install -r requirements.txt; python import_flask.py` | 0 | Flask version: 2.2.2 |
|  |  |  | `conda env create -f environment.yml (with -p temp prefix)` | 0 | created; python 3.10.22; requests version: 2.32.3; env removed |
| `pytest-none` | `main` | 1 | `python -m pytest -q --no-header` | 5 | no tests ran in 0.01s |
| `pytest-basic` | `pytest-none` | 1 | `python -m pytest -q --no-header` | 0 | 10 passed in 0.03s |
| `pytest-failing` | `pytest-basic` | 1 | `python -m pytest -q --no-header` | 1 | 3 failed, 7 passed in 0.12s |
| `app-mini` | `main` | 2 | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
|  |  |  | `Flask test client: GET /, POST digit_2/digit_7, no file, empty name, text file` | 0 | 200; Predicted digit: 2; Predicted digit: 7; errors shown |
|  |  |  | `python -m flask --app app.py run --debugger --port 9000 + curl` | 0 | GET / 200; digits 2 and 7 predicted; no-file and text-file show error |
| `lint-bad` | `app-mini` | 1 | `python -m pylint app.py model.py` | 28 | 8 messages (2xC0114, 4xC0116, W0702, R1710); pylint 7.84/10 |
| `lint-fixed` | `lint-bad` | 3 | `python -m pylint app.py model.py @ lint-fixed~2` | 12 | pylint 9.46/10 (W0702, R1710) |
|  |  |  | `python -m pylint app.py model.py @ lint-fixed~1` | 8 | pylint 9.73/10 (R1710) |
|  |  |  | `python -m pylint app.py model.py @ lint-fixed` | 0 | pylint 10.00/10 |
|  |  |  | `git diff --exit-code app-mini lint-fixed -- app.py model.py` | 0 | empty |
| `precommit-bad` | `app-mini` | 1 | `pre-commit run --all-files (config copied in, not committed)` | 1 | trailing-whitespace, end-of-file-fixer, check-yaml Failed; pylint Passed |
|  |  |  | `pre-commit run --all-files (second run)` | 1 | only check-yaml Failed |
| `precommit-fixed` | `precommit-bad` | 1 | `pre-commit install; pre-commit run --all-files` | 0 | all four hooks Passed |
|  |  |  | `git commit -m "Update notes" (trailing spaces staged)` | 1 | blocked; trailing-whitespace fixed docs/notes.md |
| `tests-weak` | `app-mini` | 1 | `python -m pytest -q --no-header` | 0 | 5 passed in 0.78s |
|  |  |  | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
| `tests-improved` | `tests-weak` | 1 | `python -m pytest -q --no-header` | 0 | 17 passed in 0.38s |
|  |  |  | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
| `ci-pass` | `tests-improved` | 1 | `yaml.safe_load(.github/workflows/ci.yml)` | 0 | valid; 5 steps |
|  |  |  | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
|  |  |  | `python -m pytest -q --no-header` | 0 | 17 passed in 0.40s |
| `ci-lint-fail` | `ci-pass` | 1 | `python -m pylint app.py model.py` | 16 | C0114 in app.py; pylint 9.73/10 |
|  |  |  | `python -m pytest -q --no-header` | 0 | 17 passed in 0.36s |
| `ci-test-fail` | `ci-pass` | 1 | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
|  |  |  | `python -m pytest -q --no-header` | 1 | assert 500 == 200; 1 failed, 17 passed in 0.52s |
| `ci-test-fixed` | `ci-test-fail` | 1 | `python -m pylint app.py model.py` | 0 | pylint 10.00/10 |
|  |  |  | `python -m pytest -q --no-header` | 0 | 18 passed in 0.37s |

## Workflow presence

Only `ci-*` branches contain `.github/workflows/ci.yml`:

```text
app-mini: no workflow
ci-lint-fail: has workflow
ci-pass: has workflow
ci-test-fail: has workflow
ci-test-fixed: has workflow
env-demo: no workflow
lint-bad: no workflow
lint-fixed: no workflow
main: no workflow
precommit-bad: no workflow
precommit-fixed: no workflow
pytest-basic: no workflow
pytest-failing: no workflow
pytest-none: no workflow
tests-improved: no workflow
tests-weak: no workflow
```

## Expected GitHub Actions runs

| Branch | Expected result |
| --- | --- |
| `ci-pass` | success |
| `ci-lint-fail` | failure at **Run Pylint**, **Run tests** skipped |
| `ci-test-fail` | failure at **Run tests** (Run Pylint passes) |
| `ci-test-fixed` | success |
| every other branch | no run (no workflow file) |
