"""Fake digit recognition model and image helpers for the demo app.

The original assignment loaded a trained TensorFlow model. This module replaces it
with a tiny deterministic numpy model so the demo runs anywhere.
"""
from functools import lru_cache

import numpy as np
from PIL import Image

INPUT_SHAPE = (1, 28, 28, 1)


class FakeDigitModel:
    """Deterministic stand-in for a trained digit classifier."""

    def digit_for(self, batch):
        """Return min(9, int(mean brightness * 10)) for a (1, 28, 28, 1) batch."""
        if batch.shape != INPUT_SHAPE:
            raise RuntimeError("unexpected input shape")
        return min(9, int(np.mean(batch) * 10))

    def predict(self, batch):
        """Return a (1, 10) score vector with 0.9 at the chosen digit."""
        scores = np.full((1, 10), 0.1 / 9)
        scores[0, self.digit_for(batch)] = 0.9
        return scores


@lru_cache(maxsize=None)
def _get_model():
    """Create the model on first use and reuse it afterwards."""
    return FakeDigitModel()


def preprocess_img(image_source):
    """Load an image and turn it into a model-ready batch.

    image_source can be a file path or a binary file-like object, such as the
    stream of an uploaded file. The image is converted to grayscale, resized to
    28x28 and scaled to float32 values in [0, 1].

    Returns a numpy array of shape (1, 28, 28, 1). Data that is not an image
    raises PIL.UnidentifiedImageError; a missing path raises FileNotFoundError.
    """
    with Image.open(image_source) as image:
        gray = image.convert("L").resize((28, 28))
    pixels = np.asarray(gray, dtype=np.float32) / 255.0
    return pixels.reshape(INPUT_SHAPE)


def predict_result(batch):
    """Return the predicted digit (0-9) for a preprocessed batch."""
    return int(np.argmax(_get_model().predict(batch)))
