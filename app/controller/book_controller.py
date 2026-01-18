from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book_schema import CreateBook, BookResponse
from app.service.book_service import BookService

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return BookService.get_books(db)

@router.post("", response_model=BookResponse)
def create_book(book: CreateBook, db: Session = Depends(get_db)):
    return BookService.create_book(db, book)

@router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = BookService.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: CreateBook, db: Session = Depends(get_db)):
    updated_book = BookService.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return updated_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    BookService.delete_book(db, book_id)
    return {"message": "Book deleted successfully!"}