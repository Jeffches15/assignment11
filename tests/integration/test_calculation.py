import pytest
from app.models.calculation import Calculation, Division, Multiplication, Subtraction

from app.models.calculation import Addition

# def get_result test
def test_get_result_not_implemented():
    calc = Calculation()
    with pytest.raises(NotImplementedError):
        calc.get_result()

# def __repr__ test
def test_calculation_repr():
    calc = Calculation(type="multiply", a=2.0, b=7.0)
    expected = "<Calculation(type=multiply, a=2.0, b=7.0)>"
    assert repr(calc) == expected

# get_result from Addition Class test
def test_addition_get_result():
    addition = Addition(a=2.5, b=3.5)
    result = addition.get_result()
    assert result == 6.0

# get_result from Subtraction Class test
def test_subtraction_get_result():
    subtraction = Subtraction(a=19, b=3.5)
    result = subtraction.get_result()
    assert result == 15.5

# get_result from Multiplication Class test
def test_multiplication_get_result():
    multiplication = Multiplication(a=6, b=7)
    result = multiplication.get_result()
    assert result == 42

# get result from Division Class test
def test_division_get_result():
    division = Division(a=10, b=2)
    result = division.get_result()
    assert result == 5

# test for: raise ValueError("The divisor 'b' cannot be zero")
def test_division_by_zero_raises_error():
    division = Division(a=10, b=0)
    with pytest.raises(ValueError, match="The divisor 'b' cannot be zero"):
        division.get_result()

