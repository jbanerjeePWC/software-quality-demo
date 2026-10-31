"""First attempt at testing model.py (kept to compare with test_model_new.py)."""
from model import predict_result, preprocess_img


def test_preprocess_img():
    batch = preprocess_img("test_images/digit_2.png")
    assert batch is not None


def test_predict_result():
    batch = preprocess_img("test_images/digit_2.png")
    assert predict_result(batch) is not None
