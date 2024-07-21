from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from utils import BOOKS, Book, find_book_id

app = FastAPI()



class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=200)
    rating: int = Field(ge=0, le=5)

    model_config = {
        'json_schema_extra': {
            "example": {
                "title": "La biblia de JavaScript",
                "author": "Douglas Crockford",
                "description": "Un libro para aprender JavaScript",
                "rating": 5
            }
        }
    }




@app.get('/books')
async def read_all_books():
    return BOOKS

@app.post('/create-book')
async def create_book(book_request: BookRequest):
   new_book = Book(**book_request.model_dump())
   new_book = find_book_id(new_book)
   BOOKS.append(new_book)

