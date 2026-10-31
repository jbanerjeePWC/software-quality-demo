"""Show which Python interpreter is running this script."""
import sys

print(f"executable: {sys.executable}")
print(f"version:    {sys.version.split()[0]}")
print(f"prefix:     {sys.prefix}")
