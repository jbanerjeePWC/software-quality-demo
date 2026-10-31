"""Improved tests for the Flask routes in app.py."""
import io
from unittest.mock import patch

import numpy as np

ERROR_TEXT = b"Could not process the image"


def upload(client, content, filename):
    """POST content to /prediction as the multipart field "file"."""
    data = {"file": (io.BytesIO(content), filename)}
    return client.post("/prediction", data=data, content_type="multipart/form-data")


def test_home_page_returns_upload_form(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'name="file"' in response.data


def test_valid_large_image_upload_new(client, make_png_bytes):
    fake_batch = np.zeros((1, 28, 28, 1), dtype=np.float32)
    # Patch the names where they are USED (app.py), not where they are defined (model.py).
    with (
        patch("app.preprocess_img", return_value=fake_batch) as mock_preprocess,
        patch("app.predict_result", return_value=2) as mock_predict,
    ):
        response = upload(client, make_png_bytes(1600, 1200), "large.png")

    assert response.status_code == 200
    assert b"Predicted digit: 2" in response.data
    mock_preprocess.assert_called_once()
    mock_predict.assert_called_once()
    assert mock_predict.call_args.args[0] is fake_batch


def test_missing_file_field_returns_controlled_error(client):
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert ERROR_TEXT in response.data


def test_empty_filename_is_handled(client):
    response = upload(client, b"", "")
    assert response.status_code == 200
    assert b"No file selected" in response.data


def test_invalid_image_bytes_return_controlled_error(client):
    response = upload(client, b"this is not an image", "notes.png")
    assert response.status_code == 200
    assert ERROR_TEXT in response.data
    assert b"Predicted digit" not in response.data
