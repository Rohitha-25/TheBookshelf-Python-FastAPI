from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import sessionLocal
from app.entity.book import Book
from app.service.book_service import BookService

router = APIRouter(prefix="/books", tags=["Books"])
book_service = BookService()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return book_service.get_all_books(db)

@router.post("/", response_model=None)
def add_book(book: dict, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)