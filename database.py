from sqlalchemy import create_engine # Importing the create_engine function from SQLAlchemy to establish a connection to the database.
from sqlalchemy.orm import sessionmaker # Importing the sessionmaker function from SQLAlchemy to create a session factory for managing database sessions.
from sqlalchemy.ext.declarative import declarative_base # Importing the declarative_base function from SQLAlchemy to create a base class for defining database models.
from urllib.parse import quote_plus

Base = declarative_base() # Creating a base class for defining database models using the declarative system of SQLAlchemy.


MYSQL_USER= "root"
MYSQL_PASSWORD= quote_plus("root@143")
MYSQL_HOST= "localhost"
MYSQL_PORT= "3306"
MYSQL_DATABASE= "my_database"

DATABASE_URL=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}" # Constructing the database URL using the provided credentials and connection details.

engine = create_engine(DATABASE_URL) # Creating an engine instance using the constructed database URL to manage the connection to the database.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Creating a session factory using the sessionmaker function, configuring it to not autocommit or autoflush, and binding it to the engine for database interactions.
def get_db():
    db = SessionLocal() # Creating a new database session using the session factory.
    try:
        yield db # Yielding the database session to be used in the application. i.e this allows the session to be used in a context where it can be automatically closed after use.
    finally:
        db.close() # Ensuring that the database session is closed after use to free up resources.

