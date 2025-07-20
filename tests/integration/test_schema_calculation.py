from datetime import datetime
from uuid import UUID, uuid4

from pydantic import ValidationError
import pytest
from app.models.calculation import Calculation
from app.models.calculation_factory import CalculationFactory
from app.models.user import User
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

# db_session: Provide a test-scoped database session
# test_user: Create and return a single test user.
def test_create_calculation_with_factory(db_session, test_user):
    # Arrange: create the input schema (CalculationCreate)
    calculation_create = CalculationCreate(
        type=CalculationType.DIVISION,  # pass enum directly
        a=42,
        b=7
    )

    # Act: create calculation instance from factory
    calc_instance = CalculationFactory.create_calculation(
        calc_type=calculation_create.type,  # already enum, no conversion needed
        a=calculation_create.a,
        b=calculation_create.b
    )
    result = calc_instance.get_result()

    # Save to DB
    db_calc = Calculation(
        user_id=test_user.id,
        type=calculation_create.type,
        a=calculation_create.a,
        b=calculation_create.b,
        result=result
    )
    db_session.add(db_calc)
    db_session.commit()
    db_session.refresh(db_calc)

    print(f"Calculation ID after commit: {db_calc.id}")
    all_calcs = db_session.query(Calculation).filter_by(user_id=test_user.id).all()
    print(f"Calculations in DB for user: {len(all_calcs)}")


    # Assert
    assert db_calc.id is not None
    assert db_calc.result == 6  # 42 / 7 = 6
    assert db_calc.a == 42
    assert db_calc.b == 7
    assert db_calc.user_id == test_user.id
    assert db_calc.type == CalculationType.DIVISION


