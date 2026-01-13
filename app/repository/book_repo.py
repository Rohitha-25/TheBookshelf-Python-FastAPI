from sqlalchemy.orm import Session
from app.entity.book import Book

class BookRepository:

    def find_all(self, db: Session):
        return db.query(Book).all()
    
    def save(self, db: Session, book: Book):
        db.add(book)
        db.commit()
        db.refresh(book)
        return book