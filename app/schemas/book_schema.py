from pydantic import BaseModel

class CreateBook(BaseModel):
    title: str
    author: str
    price: float

class BookResponse(CreateBook):
    id: int

    class Config:
        from_attributes = True