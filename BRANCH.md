# Branch `pytest-basic`

Adds test_calculator.py: plain asserts, pytest.raises, parametrize and pytest.approx.
All 10 tests pass.

- Parent branch: `pytest-none`
- Used in: Video 2 - pytest basics

## Commands

```powershell
pip install -r requirements-dev.txt
python -m pytest -q --no-header
python -m pytest -v --no-header
```

## Expected output

`python -m pytest -q --no-header` (exit code 0):

```text
..........                                                               [100%]
10 passed in 0.05s
```

`python -m pytest -v --no-header`:

```text
============================= test session starts =============================
collecting ... collected 10 items

test_calculator.py::test_add_two_positive_numbers PASSED                 [ 10%]
test_calculator.py::test_add_negative_and_positive_number PASSED         [ 20%]
test_calculator.py::test_divide_two_numbers PASSED                       [ 30%]
test_calculator.py::test_divide_by_zero_raises_error PASSED              [ 40%]
test_calculator.py::test_average_of_three_numbers PASSED                 [ 50%]
test_calculator.py::test_average_of_floats_is_approximately_correct PASSED [ 60%]
test_calculator.py::test_average_of_empty_list_raises_error PASSED       [ 70%]
test_calculator.py::test_apply_discount[100-10-90] PASSED                [ 80%]
test_calculator.py::test_apply_discount[80-25-60] PASSED                 [ 90%]
test_calculator.py::test_apply_discount[200-50-100] PASSED               [100%]

============================= 10 passed in 0.03s ==============================
```

Timings (`in 0.35s`) and object addresses vary from run to run.
