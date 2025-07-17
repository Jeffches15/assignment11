from abc import ABC

from app.database import Base


class Calculation(Base, ABC):
    """Base calculation model"""
    
    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "calculation",
        #"with_polymorphic": "*"
    }