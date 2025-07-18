from datetime import datetime, timezone
import enum
import uuid
from sqlalchemy.orm import relationship

from sqlalchemy import UUID, Column, DateTime, Enum, Float, ForeignKey

from app.models.base import Base

class CalculationType(enum.Enum):
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"

# SQLAlchemy ORM model that defines how a "calculation" is stored in the database 
class Calculation(Base):
    """Base calculation model"""

    __tablename__ = "calculations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(Enum(CalculationType), nullable=False)
    result = Column(Float, nullable=True)

    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Foreign key to User
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # user associated with calculations (1 to many relationship)
    user = relationship("User", back_populates="calculations")

    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "calculation",
    }

    def get_result(self) -> float:
        """Method to compute calculation result"""
        raise NotImplementedError

    def __repr__(self):
        return f"<Calculation(type={self.type}, a={self.a}, b={self.b})>"
    
class Addition(Calculation):
    __mapper_args__ = {
        "polymorphic_identity": CalculationType.ADDITION,
    }

    def get_result(self) -> float:
        return self.a + self.b
    
class Subtraction(Calculation):
    __mapper_args__ = {
        "polymorphic_identity": CalculationType.SUBTRACTION,
    }

    def get_result(self) -> float:
        return self.a - self.b
    
class Multiplication(Calculation):
    __mapper_args__ = {
        "polymorphic_identity": CalculationType.MULTIPLICATION,
    }

    def get_result(self) -> float:
        return self.a * self.b
    
class Division(Calculation):
    __mapper_args__ = {
        "polymorphic_identity": CalculationType.DIVISION,
    }

    def get_result(self) -> float:
        if self.b == 0 :
            raise ValueError("The divisor 'b' cannot be zero")
        return self.a / self.b