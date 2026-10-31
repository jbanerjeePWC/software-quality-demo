# quality-madness-demo

Teaching material for short screen-recorded tutorials about Python environments,
linting (pylint), pre-commit, pytest and GitHub Actions CI.

The repository is a network of branches. Each branch is a ready-made stage for one
tutorial. Some branches contain deliberately bad code, and each of those has a matching
fixed branch, so `git diff <bad> <fixed>` shows only the fix.

Every branch has a `BRANCH.md` at its root with the commands to demonstrate and the
expected output, copied from a real verification run.

Only branches whose names start with `ci-` contain a GitHub Actions workflow, so pushing
any other branch triggers no CI run.

## Branches

```text
main
 |- env-demo
 |- pytest-none -> pytest-basic -> pytest-failing
 |- app-mini
      |- lint-bad -> lint-fixed
      |- precommit-bad -> precommit-fixed
      |- tests-weak -> tests-improved -> ci-pass
                                          |- ci-lint-fail
                                          |- ci-test-fail -> ci-test-fixed
```

| Branch | Parent | Purpose | Tutorial (video) |
| --- | --- | --- | --- |
| `env-demo` | `main` | Python, venv, conda and requirements.txt; unpinned Werkzeug breaks Flask 2.2.2 | 1 - Python environments |
| `pytest-none` | `main` | Correct calculator module, no tests yet | 2 - pytest basics |
| `pytest-basic` | `pytest-none` | 10 passing tests: assert, raises, parametrize, approx | 2 - pytest basics |
| `pytest-failing` | `pytest-basic` | Bug in apply_discount; the 3 discount tests fail | 2 - pytest basics |
| `app-mini` | `main` | Clean mini Flask digit app with a fake numpy model, pylint 10.00/10 | Base for 3-6 |
| `lint-bad` | `app-mini` | Exactly eight pylint messages (7.84/10) | 3 - pylint |
| `lint-fixed` | `lint-bad` | Three fix commits back to 10.00/10 | 3 - pylint |
| `precommit-bad` | `app-mini` | Messy Markdown/YAML files, no pre-commit config | 4 - pre-commit |
| `precommit-fixed` | `precommit-bad` | pre-commit config added, files cleaned, all hooks pass | 4 - pre-commit |
| `tests-weak` | `app-mini` | Beginner tests that pass for the wrong reasons | 5 - better tests |
| `tests-improved` | `tests-weak` | Fixtures, real PNGs, mocks; 17 tests pass | 5 - better tests |
| `ci-pass` | `tests-improved` | GitHub Actions workflow; green | 6 - GitHub Actions CI |
| `ci-lint-fail` | `ci-pass` | Missing module docstring; CI fails at Run Pylint | 6 - GitHub Actions CI |
| `ci-test-fail` | `ci-pass` | Regression test for RuntimeError; CI fails at Run tests | 6 - GitHub Actions CI |
| `ci-test-fixed` | `ci-test-fail` | RuntimeError caught; CI green again | 6 - GitHub Actions CI |

Verified commands and results for every branch are in [VERIFIED.md](VERIFIED.md).
