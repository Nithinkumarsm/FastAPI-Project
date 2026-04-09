from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [ # Sampple database of books in list
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell"
    }
]

app = FastAPI()

@app.get("/book")
def search_books():
    return books

#Note in both put and post we use pydantic models to validate the incoming data. In the case of POST, we create a new book entry, while in PUT, we update an existing book entry based on the provided ID.

@app.get("/book/{book_id}")
def search_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
         return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") # If the book is not found, we raise an HTTPException with a 404 status code and a detail message indicating that the book was not found.


class add_book(BaseModel):
    id: int
    title: str
    author: str

@app.post("/book")
def add_books(book: add_book):
    new_book = book.model_dump() # model_dump() is a method provided by Pydantic that converts the Pydantic model instance into a dictionary. This allows us to easily manipulate the data and add it to our list of books.
    books.append(new_book)


class update_book(BaseModel):
    title: str
    author: str


@app.put("/book/{book_id}")
def update_books(book_id: int, updated: update_book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated.title
            book["author"] = updated.author
            return book
                
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return book
            return{"message": "Your book is deleted"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 
