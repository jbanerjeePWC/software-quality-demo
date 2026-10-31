# Branch `env-demo`

Shows why Python projects need isolated environments and pinned requirements.
Covers `python -m venv`, `pip install -r`, a Werkzeug version conflict and conda.

- Parent branch: `main`
- Used in: Video 1 - Python environments (venv, conda, requirements.txt)

## Files

| File | What it shows |
| --- | --- |
| `whichpython.py` | which interpreter is running (`sys.executable`, version, `sys.prefix`) |
| `hello_requests.py` | fails with `ModuleNotFoundError` until `requests` is installed |
| `requirements.txt` | pinned requests, Flask 2.2.2 and Werkzeug 2.2.2 |
| `requirements-unpinned.txt` | only `flask==2.2.2`, so pip pulls the newest Werkzeug |
| `import_flask.py` | imports Flask and prints its version |
| `environment.yml` | conda version of the same idea |

## Demo 1: venv, activation, missing package

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1        # macOS/Linux: source .venv/bin/activate
python whichpython.py
python hello_requests.py
pip install -r requirements.txt
python hello_requests.py
```

Expected (verified in a fresh venv; your paths differ):

```text
executable: %TEMP%\qmd\v-env-a\Scripts\python.exe
version:    3.10.22
prefix:     %TEMP%\qmd\v-env-a
```

`python hello_requests.py` before installing (exit code 1):

```text
Traceback (most recent call last):
  File "%TEMP%\qmd\clones\env-demo\hello_requests.py", line 2, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

After `pip install -r requirements.txt` (exit code 0):

```text
requests version: 2.32.3
```

## Demo 2: an unpinned dependency breaks the app

In a new, empty venv:

```powershell
pip install -r requirements-unpinned.txt
pip list
python import_flask.py
```

pip installs `Werkzeug 3.1.9` (Flask 2.2.2 only asks for `Werkzeug>=2.2.2`), and the
import fails (exit code 1):

```text
Traceback (most recent call last):
  File "%TEMP%\qmd\clones\env-demo\import_flask.py", line 4, in <module>
    import flask  # the import itself is what breaks when Werkzeug is too new
  File "%TEMP%\qmd\v-env-b\lib\site-packages\flask\__init__.py", line 5, in <module>
    from .app import Flask as Flask
  File "%TEMP%\qmd\v-env-b\lib\site-packages\flask\app.py", line 30, in <module>
    from werkzeug.urls import url_quote
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (%TEMP%\qmd\v-env-b\lib\site-packages\werkzeug\urls.py)
```

The key line:

```text
ImportError: cannot import name 'url_quote' from 'werkzeug.urls'
```

## Demo 3: pinning fixes it

```powershell
pip install -r requirements.txt     # downgrades Werkzeug 3.1.9 -> 2.2.2
python import_flask.py
```

Expected (exit code 0; same result in a fresh venv):

```text
flask module: flask
Flask version: 2.2.2
```

## Demo 4: conda

```powershell
conda env create -f environment.yml
conda activate demo-env
python hello_requests.py
conda deactivate
conda env remove -n demo-env -y
```

Verified (created under a temporary prefix with `-p` so an existing `demo-env` was not touched):
`conda env create` exit code 0, Python 3.10.22, and `python hello_requests.py` printed:

```text
requests version: 2.32.3
```

Run `conda env create` from a shell where `conda init` has been done (Anaconda Prompt or an
initialised PowerShell). Calling `conda.exe` directly from a non-initialised shell failed at the
pip step with `Failed to run 'conda activate ...'`.
