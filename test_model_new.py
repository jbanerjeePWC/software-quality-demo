"""Improved tests for model.py."""
import io
from pathlib import Path
from unittest.mock import Mock, patch

import numpy as np
import pytest

from model import predict_result, preprocess_img

IMAGES = Path(__file__).resolve().parent / "test_images"


def test_preprocess_img_shape_dtype_and_range():
    batch = preprocess_img(IMAGES / "digit_2.png")
    assert batch.shape == (1, 28, 28, 1)
    assert batch.dtype == np.float32
    assert 0.0 <= batch.min() <= batch.max() <= 1.0


@pytest.mark.parametrize(("width", "height"), [(10, 10), (2000, 1500)])
def test_preprocess_resizes_small_and_large_images(make_png_bytes, width, height):
    batch = preprocess_img(io.BytesIO(make_png_bytes(width, height)))
    assert batch.shape == (1, 28, 28, 1)


def test_predict_result_returns_index_of_highest_score():
    stub_model = Mock()
    stub_model.predict.return_value = np.array([[0.0, 0.1, 0.0, 0.0, 0.7, 0.1, 0.0, 0.0, 0.1, 0.0]])
    with patch("model._get_model", return_value=stub_model):
        assert predict_result(np.zeros((1, 28, 28, 1))) == 4


def test_preprocess_missing_path_raises_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        preprocess_img(tmp_path / "does_not_exist.png")


def test_predict_digit_2_image_end_to_end():
    assert predict_result(preprocess_img(IMAGES / "digit_2.png")) == 2


def test_predict_digit_7_image_end_to_end():
    assert predict_result(preprocess_img(IMAGES / "digit_7.png")) == 7
