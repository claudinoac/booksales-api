from apps.book.models import Book
from apps.base.repository import BaseRepository


class BookRepository(BaseRepository):
    model = Book

    def get_book_by_author_and_title(self, author, title):
        return self.db_session.query(self.model).filter_by(
            author=author, title=title
        ).first()

    def get_books_by_id_list(self, id_list):
        return self.db_session.query(Book).filter(Book.id.in_(id_list)).all()
