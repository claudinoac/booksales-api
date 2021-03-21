from book.models import Book
from base.repository import BaseRepository


class BookRepository(BaseRepository):
    model = Book

    def get_book_by_author_and_title(self, author, title):
        return self.db_session.query(self.model).filter_by(
            author=author, title=title
        ).first()
