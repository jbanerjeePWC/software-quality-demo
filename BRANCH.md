# Branch `lint-fixed`

Fixes every lint-bad message in three small commits, back to 10.00/10.
The final app.py and model.py are identical to app-mini.

- Parent branch: `lint-bad`
- Used in: Video 3 - Linting with pylint

## Commits

1. `Setup: add module and function docstrings to address pylint`
2. `Setup: Removed bare exception` (bare `except:` becomes `except (KeyError, OSError, ValueError):`)
3. `Setup: Ensured return from all paths` (the except branch returns the error page)

## Commands

```powershell
git log --oneline lint-bad..lint-fixed
git diff lint-bad lint-fixed -- app.py model.py
git checkout lint-fixed~2
python -m pylint app.py model.py
git checkout lint-fixed~1
python -m pylint app.py model.py
git checkout lint-fixed
python -m pylint app.py model.py
git diff app-mini lint-fixed -- app.py model.py      # empty
```

## Score ladder (verified after each commit)

| Step | Commit | Score | Exit code | Remaining messages |
| --- | --- | --- | --- | --- |
| start | lint-bad | 7.84/10 | 28 | 8 messages (see lint-bad) |
| 1 | add docstrings | 9.46/10 | 12 | `W0702`<br>`R1710` |
| 2 | removed bare exception | 9.73/10 | 8 | `R1710` |
| 3 | return from all paths | 10.00/10 | 0 | none |

Final pylint output:

```text
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.73/10, +0.27)
```

The `(previous run: ...)` part of pylint's score line depends on your local pylint
history and will differ; the messages and the score itself are fixed.

`git diff --exit-code app-mini lint-fixed -- app.py model.py` prints nothing and exits
0. Only BRANCH.md differs between app-mini and lint-fixed.
