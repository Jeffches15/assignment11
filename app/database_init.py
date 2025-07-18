# initialize database
# used in conftest for testing purposes

# Imports the SQLAlchemy engine that connects to your PostgreSQL database.
# The engine contains connection info from settings.DATABASE_URL.
from app.database import engine

# Base is the declarative base that holds metadata about all your SQLAlchemy models.
# Any models that inherit from Base will be included in table creation.
from app.models.user import Base

def init_db():
    # This scans all the models that inherit from Base and issues the SQL CREATE TABLE statements to the database.
    # It’s the equivalent of "Apply your models to the database."
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    init_db() # pragma: no cover