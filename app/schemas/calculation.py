from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

# They define the structure, 
# validation rules, and documentation metadata for the data your API will accept and return.

# FastAPI and Pydantic can automatically serialize it to JSON as just the string
class CalculationType(str, Enum):
    """Calculation types"""
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"

class CalculationBase(BaseModel):
    """Base Schema with common Calculation fields"""

    type: CalculationType = Field(
        ..., # This field has no default value — it must be provided when the model is created
        description="Type of calculation (ex: addition, subtraction, multiplication, division)",
        example="addition"
    )

    a: float = Field(
        ..., 
        description="First number", 
        example=10.5
    )

    b: float = Field(
        ..., 
        description="Second number", 
        example=2
    )

# Client sends this to create
class CalculationCreate(CalculationBase):
    """Schema that creates a new calculation"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "type": "addition",
                "a": 4.5,
                "b": 3,
            }
        }
    )

# Server sends this back to Client for reference
class CalculationRead(CalculationBase):
    """Schema that sends back calculation"""
    
    id: UUID = Field(
        ...,
        description="Unique identifier for the calculation",
        example="123e4567-e89b-12d3-a456-426614174000"
    )

    user_id: UUID = Field(
        ...,
        description="Unique identifier of the user who owns this calculation",
        example="123e4567-e89b-12d3-a456-426614174002"
    )

    result: float = Field(
        ...,
        description="Result of operation between first number and second number",
        example=12.5
    )

    created_at: datetime = Field(..., description="Time the calculation was created")
    updated_at: datetime = Field(..., description="Time the calculation was last updated")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174001",
                "user_id": "123e4567-e89b-12d3-a456-426614174045",
                "type": "addition",
                "a": 4.5,
                "b": 3,
                "result": 7.5,
                "created_at": "2025-07-16T00:00:00",
                "updated_at": "2025-07-16T00:00:00"
            }
        }
    )
