"""Fails with ModuleNotFoundError until the requests package is installed."""
import requests

print("requests version: " + requests.__version__)
