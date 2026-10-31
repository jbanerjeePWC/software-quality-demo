"""Tests for calculator.py."""
import pytest

from calculator import add, apply_discount, average, divide


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_and_positive_number():
    assert add(-4, 10) == 6


def test_divide_two_numbers():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(1, 0)


def test_average_of_three_numbers():
    assert average([1, 2, 3]) == 2


def test_average_of_floats_is_approximately_correct():
    # 0.1 + 0.2 + 0.3 is not exactly 0.6 in floating point, so compare approximately.
    assert average([0.1, 0.2, 0.3]) == pytest.approx(0.2)


def test_average_of_empty_list_raises_error():
    with pytest.raises(ValueError, match="empty list"):
        average([])


@pytest.mark.parametrize(
    ("price", "percent", "expected"),
    [
        (100, 10, 90),
        (80, 25, 60),
        (200, 50, 100),
    ],
)
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
