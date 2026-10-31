"""Regression test: a model runtime failure must not crash the request."""
import io
from unittest.mock import patch

import numpy as np


def test_prediction_runtime_error_new(client, make_png_bytes, monkeypatch):
    # Behave like production: in TESTING mode Flask re-raises unhandled exceptions
    # inside the test; with this off, they become an HTTP 500 response instead.
    monkeypatch.setitem(client.application.config, "PROPAGATE_EXCEPTIONS", False)
    fake_batch = np.zeros((1, 28, 28, 1), dtype=np.float32)
    failure = RuntimeError("simulated model runtime failure")
    data = {"file": (io.BytesIO(make_png_bytes(64, 64)), "digit.png")}

    with (
        patch("app.preprocess_img", return_value=fake_batch),
        patch("app.predict_result", side_effect=failure),
    ):
        response = client.post("/prediction", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"Could not process the image" in response.data
