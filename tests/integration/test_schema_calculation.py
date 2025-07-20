from datetime import datetime
from uuid import UUID, uuid4

from pydantic import ValidationError
import pytest
from app.schemas.calculation import CalculationCreate, CalculationRead, CalculationType

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

def test_calculation_read_schema_valid():
    data = {
        "id": "123e4567-e89b-12d3-a456-426614174001",
        "user_id": "123e4567-e89b-12d3-a456-426614174045",
        "type": "addition",
        "a": 4.5,
        "b": 3,
        "result": 7.5,
        "created_at": "2025-07-16T00:00:00",
        "updated_at": "2025-07-16T00:00:00"
    }

    calc = CalculationRead(**data)

    assert calc.id == UUID(data["id"])
    assert calc.user_id == UUID(data["user_id"])
    assert calc.type == CalculationType.ADDITION
    assert calc.a == 4.5
    assert calc.b == 3
    assert calc.result == 7.5
    assert calc.created_at == datetime.fromisoformat(data["created_at"])
    assert calc.updated_at == datetime.fromisoformat(data["updated_at"])