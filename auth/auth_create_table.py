from auth_database import engine,Base    # Importing the engine and Base class from the database module, which is used as a base for defining database models.
from model import User

Base.metadata.create_all(bind=engine) # Creating all tables in the database based on the defined models, using the engine to manage the connection to the database. 
