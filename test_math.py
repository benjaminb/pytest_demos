import pytest

def square(x):
    return x**2

def division(numerator, denominator):
    return numerator / denominator

def test_square():
    assert square(2) == square(-2) == 4

def test_division():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

