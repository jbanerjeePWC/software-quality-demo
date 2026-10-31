# Branch `pytest-failing`

One commit introduces a bug in apply_discount (`percent / 10` instead of `percent / 100`).
The three parametrized discount tests fail; the other seven still pass.

- Parent branch: `pytest-basic`
- Used in: Video 2 - pytest basics

## Commands

```powershell
git diff pytest-basic pytest-failing -- calculator.py
python -m pytest -q --no-header
```

## Expected output

Exit code 1. Exactly 3 tests fail, all of them `test_apply_discount[...]`.
Excerpt:

```text
_______________________ test_apply_discount[100-10-90] ________________________

price = 100, percent = 10, expected = 90

    @pytest.mark.parametrize(
        ("price", "percent", "expected"),
        [
            (100, 10, 90),
            (80, 25, 60),
            (200, 50, 100),
        ],
    )
    def test_apply_discount(price, percent, expected):
>       assert apply_discount(price, percent) == expected
E       assert 0.0 == 90
E        +  where 0.0 = apply_discount(100, 10)

test_calculator.py:47: AssertionError

(two more failure blocks of the same shape)

FAILED test_calculator.py::test_apply_discount[100-10-90] - assert 0.0 == 90
FAILED test_calculator.py::test_apply_discount[80-25-60] - assert -120.0 == 60
FAILED test_calculator.py::test_apply_discount[200-50-100] - assert -800.0 ==...
3 failed, 7 passed in 0.15s
```

Timings (`in 0.35s`) and object addresses vary from run to run.
