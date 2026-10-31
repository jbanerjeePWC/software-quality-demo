"""A tiny calculator module used to demonstrate pytest."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers.

    Raises:
        ValueError: if numbers is empty.
    """
    if not numbers:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)


def apply_discount(price, percent):
    """Return price reduced by percent (20 means 20% off)."""
    return price * (1 - percent / 100)
