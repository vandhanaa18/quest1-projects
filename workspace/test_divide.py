import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestDivideFunction:

    # === Normal Cases ===
    def test_division_positive_numbers(self):
        assert divide(10, 2) == 5.0
        assert divide(7, 3) == pytest.approx(2.3333333)
        
    def test_division_negative_numbers(self):
        assert divide(-10, -2) == 5.0
        assert divide(10, -2) == -5.0
        assert divide(-7, 3) == pytest.approx(-2.3333333)

    def test_division_zero_as_a(self):
        assert divide(0, 5) == 0.0
        
    # === Edge Cases ===
    @pytest.mark.parametrize("test_case", [1/0])
    def test_one_divided_by_self(self):
        result = divide(42, 7)
        expected = float(test_case[0] / test_case[1]) if isinstance(test_case, tuple) else pytest.approx(float('inf'))
