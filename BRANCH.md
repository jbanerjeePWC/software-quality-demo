# Branch `precommit-fixed`

Adds .pre-commit-config.yaml (trailing-whitespace, end-of-file-fixer, check-yaml,
local pylint hook) and cleans the three messy files. All four hooks pass.

- Parent branch: `precommit-bad`
- Used in: Video 4 - pre-commit hooks

## Commands

```powershell
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```

Then show the hook blocking a commit:

```powershell
Add-Content docs/notes.md "Added during the demo.   "
git add docs/notes.md
git commit -m "Update notes"
git status --short
git diff
```

## Expected output

`pre-commit install`:

```text
pre-commit installed at .git\hooks\pre-commit
```

`pre-commit run --all-files` (exit code 0):

```text
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Pylint application files.................................................Passed
```

`git commit -m "Update notes"` with a trailing-whitespace line staged (exit code
1; the commit is blocked):

```text
Trim Trailing Whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing docs/notes.md

Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Pylint application files.................................................Passed
```

`git status --short` (staged version still has the spaces, working copy was fixed):

```text
MM docs/notes.md
```

`git diff` (trailing spaces shown as `·`):

```diff
diff --git a/docs/notes.md b/docs/notes.md
index 23adb18..1434c3a 100644
--- a/docs/notes.md
+++ b/docs/notes.md
@@ -4,4 +4,4 @@ Some lines end with invisible spaces.
 The app predicts a digit from an uploaded image.
 Run pylint before every commit.
 Nobody remembered the final newline.
-Added during the demo.···
+Added during the demo.
```

`git add docs/notes.md` and `git commit` again then succeed.

Note: pre-commit 4.x prints
`[WARNING] repo https://github.com/pre-commit/pre-commit-hooks uses deprecated stage names`
the first time it installs pre-commit-hooks v3.4.0. The hooks still work; `pre-commit autoupdate`
would remove the warning but changes the pinned `rev`.
