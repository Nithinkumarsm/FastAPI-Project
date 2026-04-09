from datetime import date

from fastapi import FastAPI,Depends
from database import get_db,engine,Base
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class Bookstore(BaseModel): 
    id: int
    title: str
    author: str
    published_date: date

@app.post("/books/")
def create_book(book: Bookstore, db: Session = Depends(get_db)):
    new_book = model.Book(id=book.id, title=book.title, author=book.author, published_date=book.published_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book) # Refreshing the new_book instance to get the updated state from the database, which includes any auto-generated fields like the primary key.
    return new_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first() # Querying the database to find the book with the specified id.
    if book:
        db.delete(book) # Deleting the found book from the database.
        db.commit() # Committing the transaction to save the changes to the database.
        return {"message": "Book deleted successfully"} # Returning a success message if the book was found and deleted.
    else:
        return {"message": "Book not found"} # Returning a not found message if no book with the specified id exists in the database.
    

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    books = db.query(model.Book).all() # Querying the database to retrieve all books.
    return books # Returning the list of books retrieved from the database.