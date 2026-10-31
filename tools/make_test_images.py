"""Generate the uniform-gray sample images in test_images/.

The fake model predicts min(9, int(mean_brightness * 10)), so a gray level of
round(digit * 25.5 + 13) makes it predict exactly that digit.

Usage: python tools/make_test_images.py
"""
from pathlib import Path

from PIL import Image

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "test_images"
SIZE = (280, 280)
DIGITS = (2, 7)


def gray_level(digit):
    """Return the gray level (0-255) that the fake model maps to digit."""
    return round(digit * 25.5 + 13)


def main():
    """Write one PNG per digit in DIGITS."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    for digit in DIGITS:
        path = OUTPUT_DIR / f"digit_{digit}.png"
        Image.new("L", SIZE, color=gray_level(digit)).save(path)
        print(f"wrote {path.name} (gray level {gray_level(digit)})")


if __name__ == "__main__":
    main()
