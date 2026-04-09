from database import Base # Importing the Base class from the database module, which is used as a base for defining database models.
from sqlalchemy import Column, Integer, String, Date # Importing necessary column types from SQLAlchemy to define the structure of the database model.

class Book(Base): # Defining a Book class that inherits from the Base class, representing a database model for a book.
    __tablename__ = "books" # Specifying the name of the database table that this model corresponds to.

    id = Column(Integer, primary_key=True, index=True) # Defining an id column as an integer, which is the primary key and indexed for faster queries.
    title = Column(String(255), nullable=False) # Defining a title column as a string with a maximum length of 255 characters, which cannot be null.
    author = Column(String(255), nullable=False) # Defining an author column as a string with a maximum length of 255 characters, which cannot be null.
    published_date = Column(Date, nullable=True) # Defining a published_date column as a Date type, which can be null.

