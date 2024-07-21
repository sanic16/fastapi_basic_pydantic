from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from utils import BOOKS, Book, find_book_id

app = FastAPI()



class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=200)
    rating: int = Field(ge=0, le=5)
    published_year : int = Field(gt=1999, lt=2031)

    model_config = {
        'json_schema_extra': {
            "example": {
                "title": "La biblia de JavaScript",
                "author": "Douglas Crockford",
                "description": "Un libro para aprender JavaScript",
                "rating": 5,
                "published_year": 2024
            }
        }
    }




@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_id}')
async def read_book(book_id: int = Path(gt=0, description="The ID of the book you want to read")):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get('/books/')
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get('/books/publish/')
async def read_books_by_publish_date(published_year: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_year == published_year:
            books_to_return.append(book)
        
    return books_to_return

@app.post('/create-book')
async def create_book(book_request: BookRequest):
   new_book = Book(**book_request.model_dump())
   new_book = find_book_id(new_book)
   BOOKS.append(new_book)
   return new_book

@app.put('/books/update_book')
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete('/books/{book_id}')
async def delete_book(book_id: int = Path(gt=0, description="The ID of the book you want to delete")):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break

    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")