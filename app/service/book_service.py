from sqlalchemy.orm import Session
from app.repository.book_repo import BookRepository
from app.entity.book import Book
from app.schemas.book_schema import CreateBook

class BookService:

    # @staticmethod acts as the dependency injection. equivalent to @Autowired in spring.
    # def __init__(self):
    #     self.repository = BookRepository()

    @staticmethod
    def get_books(db: Session):
        return BookRepository.find_all(db)
    
    @staticmethod
    def get_book_by_id(db:Session, book_id: int):
        return BookRepository.find_by_id(db, book_id)
    
    @staticmethod
    def create_book(db: Session, book_data: CreateBook):
        book = Book(title=book_data.title, author=book_data.author, price=book_data.price)
        return BookRepository.save(db, book)
    
    @staticmethod
    def update_book(db: Session, book_id: int, book_data: CreateBook):
        book = BookRepository.find_by_id(db, book_id)
        if not book:
            return None
        
        book.title = book_data.title
        book.author = book_data.author
        book.price = book_data.price

        return BookRepository.save(db, book)
    
    @staticmethod
    def delete_book(db: Session, book_id: int):
        book = BookRepository.find_by_id(db, book_id)
        if book:
            BookRepository.delete(db, book)