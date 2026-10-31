# Branch `ci-test-fixed`

Adds RuntimeError to the exceptions caught in prediction(). The regression test now
passes and CI is green again.

- Parent branch: `ci-test-fail`
- Used in: Video 6 - Continuous integration with GitHub Actions

## Commands

```powershell
git diff ci-test-fail ci-test-fixed -- app.py
```

```powershell
python -m pip install -r requirements.txt
python -m pip install pylint pytest
python -m pylint app.py model.py
python -m pytest -q --no-header
```

## Expected output

Pylint (exit code 0):

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Pytest (exit code 0):

```text
..................                                                       [100%]
18 passed in 0.40s
```

Expected in GitHub Actions: the run succeeds.
