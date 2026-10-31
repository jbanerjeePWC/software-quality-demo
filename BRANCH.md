# Branch `precommit-bad`

Adds messy files (trailing spaces, missing final newline, broken YAML) and no
.pre-commit-config.yaml. app.py and model.py stay clean (pylint 10.00/10).

- Parent branch: `app-mini`
- Used in: Video 4 - pre-commit hooks

## Messy files

| File | Problem |
| --- | --- |
| `docs/notes.md` | three lines end with trailing spaces; no final newline |
| `config/defaults.yaml` | valid YAML, trailing whitespace on two lines |
| `config/settings.yaml` | broken YAML: the `[png, jpg, jpeg` list is never closed |

## Commands

Copy the config from the fixed branch without committing it, then run the hooks:

```powershell
pip install -r requirements-dev.txt
git show precommit-fixed:.pre-commit-config.yaml > .pre-commit-config.yaml
pre-commit run --all-files
git status --short
pre-commit run --all-files
```

(In Windows PowerShell 5.1, `>` writes UTF-16; use
`git show precommit-fixed:.pre-commit-config.yaml | Set-Content -Encoding utf8 .pre-commit-config.yaml`
or check out the file with `git checkout precommit-fixed -- .pre-commit-config.yaml`
followed by `git reset .pre-commit-config.yaml`.)

## Expected output

First run (exit code 1; downloads and installs the hook repo, about
36 seconds the first time):

```text
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[WARNING] repo `https://github.com/pre-commit/pre-commit-hooks` uses deprecated stage names (commit, push) which will be removed in a future version.  Hint: often `pre-commit autoupdate --repo https://github.com/pre-commit/pre-commit-hooks` will fix this.  if it does not -- consider reporting an issue to that repo.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Trim Trailing Whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing config/defaults.yaml
Fixing docs/notes.md

Fix End of Files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing docs/notes.md

Check Yaml...............................................................Failed
- hook id: check-yaml
- exit code: 1

while parsing a flow sequence
  in "config/settings.yaml", line 4, column 23
expected ',' or ']', but got ':'
  in "config/settings.yaml", line 5, column 7

Pylint application files.................................................Passed
```

Failing hooks on the first run: trailing-whitespace, end-of-file-fixer, check-yaml. Pylint passes.

`git status --short` afterwards:

```text
 M config/defaults.yaml
 M docs/notes.md
?? .pre-commit-config.yaml
```

Second run (exit code 1): the auto-fixable problems are gone, check-yaml
still fails because broken YAML cannot be fixed automatically:

```text
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Failed
- hook id: check-yaml
- exit code: 1

while parsing a flow sequence
  in "config/settings.yaml", line 4, column 23
expected ',' or ']', but got ':'
  in "config/settings.yaml", line 5, column 7

Pylint application files.................................................Passed
```
