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
    with Image.open(image_source) as image:
        gray = image.convert("L").resize((28, 28))
    pixels = np.asarray(gray, dtype=np.float32) / 255.0
    return pixels.reshape(INPUT_SHAPE)


def predict_result(batch):
    return int(np.argmax(_get_model().predict(batch)))
