from sqlalchemy.orm import Session
from app.repository.book_repo import BookRepository
from app.entity.book import Book

class BookService:

    def __init__(self):
        self.repository = BookRepository()

    def get_all_books(self, db: Session):
        return self.repository.find_all(db)
    
    def create_book(self, db: Session, data: dict):
        book = Book(title=data["title"], author=data["author"])
        return self.repository.save(db, book)