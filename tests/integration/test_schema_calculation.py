from uuid import uuid4

from pydantic import ValidationError
import pytest
from app.schemas.calculation import CalculationCreate, CalculationType

def test_calculation_create_schema_valid():
    schema = CalculationCreate(type="addition", a=5, b=3)
    assert schema.type == CalculationType.ADDITION
    assert schema.a == 5
    assert schema.b == 3


def test_calculation_create_invalid_type():
    data = {
        "a": 1,
        "b": 2,
        "type": "EXPONENTIATION",  # Invalid enum
        "user_id": str(uuid4())
    }

    with pytest.raises(ValidationError):
        CalculationCreate(**data)

def test_calculation_create_missing_field():
    data = {
        "a": 1,
        "b": 2,
        # Missing 'type'
        "user_id": str(uuid4())
    }

    with pytest.raises(ValidationError):
        CalculationCreate(**data)