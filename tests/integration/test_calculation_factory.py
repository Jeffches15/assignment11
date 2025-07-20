# tests/unit/test_calculation_factory.py

import pytest
from app.models.calculation_factory import CalculationFactory
from app.models.calculation import CalculationType
from app.models.calculation import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize("calc_type, a, b, expected_class, expected_result", [
    (CalculationType.ADDITION, 2, 3, Addition, 5),
    (CalculationType.SUBTRACTION, 5, 2, Subtraction, 3),
    (CalculationType.MULTIPLICATION, 3, 4, Multiplication, 12),
    (CalculationType.DIVISION, 10, 2, Division, 5),
])
def test_calculation_factory(calc_type, a, b, expected_class, expected_result):
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    assert isinstance(calc, expected_class)
    assert calc.get_result() == expected_result

def test_calculation_factory_invalid_type():
    with pytest.raises(ValueError, match="Unknown calculation type"):
        CalculationFactory.create_calculation("invalid", 1, 2)
