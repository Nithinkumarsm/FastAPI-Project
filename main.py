from fastapi import FastAPI 
from typing import Optional # Optional is used to indicate that a query parameter is optional (in this case, age can be optional)
from pydantic import BaseModel # Pydantic is used for data validation and serialization. It allows us to define data models that can be used to validate incoming request data and serialize outgoing response data.



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World from FastAPI!"}

@app.get("/greet")
def greet():
    return {"message": "Hello Nithin from FastAPI!"}

# @app.get("/greet/{name}") # Path parameter to greet a specific name
# def greet_name(name: str):
#     return {"message": f"Hello {name} from FastAPI!"}

@app.get("/greet/{name}") 
def greet_name(name: str,age: int): # Query parameter to greet a specific name with age (in the URL, it will be http://127.0.0.1:8000/greet/{name}?age=30)
    return {"message": f"Hello {name}, you are {age}. Welcome to FastAPI!"}

# @app.get("/greet/{name}") 
# def greet_name(name: str,age: Optional[int] = None): # Query parameter to greet a specific name with optional age (in the URL, it will be http://127.0.0.1:8000/greet/{name}?
#     if age is None:
#         return {"message": f"Hello {name}, I don't know your age. Welcome to FastAPI!"}
#     return {"message": f"Hello {name}, you are {age}. Welcome to FastAPI!"}

#Note: query parameter starts with ? and is followed by key=value pairs, multiple query parameters can be separated by & (e.g., http://127.0.0.1:8000/greet/John?age=30)

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student): #calling class Student as a parameter to the function create_student.
    return{
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }