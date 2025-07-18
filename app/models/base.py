# app/models/base.py

# shared Base for user.py and calculation.py
# if User and Calculation are being defined on two different bases, 
    # then this breaks SQLAlchemy relationships.
from sqlalchemy.orm import declarative_base

Base = declarative_base()
