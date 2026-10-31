"""Import Flask and print its installed version."""
from importlib.metadata import version

import flask  # the import itself is what breaks when Werkzeug is too new

print("flask module: " + flask.__name__)
print("Flask version: " + version("flask"))
