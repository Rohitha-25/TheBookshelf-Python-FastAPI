from sqlalchemy.orm import Session
from app.entity.book import Book

class BookRepository:

    @staticmethod
    def find_all(db: Session):
        return db.query(Book).all()
    
    @staticmethod
    def find_by_id(db: Session, book_id: int):
        return db.query(Book).filter(Book.id == book_id).first()
    
    @staticmethod
    def save(db: Session, book: Book):
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
    
    @staticmethod
    def delete(db: Session, book: Book):
        db.delete(book)
        db.commit()