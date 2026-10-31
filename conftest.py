"""Shared pytest fixtures for the improved tests."""
import io

import pytest
from PIL import Image

from app import app as flask_app


@pytest.fixture
def client():
    """A Flask test client with testing mode switched on."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client


@pytest.fixture
def make_png_bytes():
    """Return a function that builds a real PNG image in memory."""

    def _make_png_bytes(width, height, gray=128):
        buffer = io.BytesIO()
        Image.new("L", (width, height), color=gray).save(buffer, format="PNG")
        return buffer.getvalue()

    return _make_png_bytes
