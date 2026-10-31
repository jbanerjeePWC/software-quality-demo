"""First attempt at testing the Flask app (kept to compare with test_app_new.py)."""
import io

from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_prediction_upload():
    client = app.test_client()
    data = {"file": (io.BytesIO(b"not an image " * 1000), "large.png")}
    response = client.post("/prediction", data=data, content_type="multipart/form-data")
    # WEAK ON PURPOSE: this passes for the wrong reason. The upload is not a real
    # image, so the app shows its error message, but result.html always contains
    # the heading "Prediction", even on error.
    assert b"Prediction" in response.data


def test_missing_file():
    client = app.test_client()
    response = client.post("/prediction")
    # Also weak: the word "Prediction" is on the page whether or not anything worked.
    assert b"Prediction" in response.data
