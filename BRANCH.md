# Branch `ci-pass`

Adds .github/workflows/ci.yml: on every push it installs dependencies, runs pylint and
then pytest on Python 3.10. Everything passes.

- Parent branch: `tests-improved`
- Used in: Video 6 - Continuous integration with GitHub Actions

Only `ci-*` branches contain the workflow, so pushing any other branch triggers nothing.

## Workflow steps

1. Check out the code
2. Set up Python 3.10
3. Install dependencies (`requirements.txt`, then unpinned `pylint pytest`)
4. Run Pylint: `python -m pylint app.py model.py`
5. Run tests: `python -m pytest -q --no-header`

## Same steps locally

```powershell
python -m pip install -r requirements.txt
python -m pip install pylint pytest
python -m pylint app.py model.py
python -m pytest -q --no-header
```

## Expected output

YAML check (`yaml.safe_load` on the workflow; PyYAML reads the `on:` key as `True`):

```text
name: CI
triggers: ['push', 'pull_request', 'workflow_dispatch']
steps: ['Check out the code', 'Set up Python 3.10', 'Install dependencies', 'Run Pylint', 'Run tests']
```

Pylint (exit code 0):

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Pytest (exit code 0):

```text
.................                                                        [100%]
17 passed in 0.56s
```

Expected in GitHub Actions: the `CI` workflow run for `ci-pass` succeeds; all steps are green.
