from settings.development import DATABASE
from book.models import Book

class BookRepository:
    db_session = None

    def __init__(self, db_session):
        self.db_session = db_session

    def create_book(self, command):
       instance = Book(**command.Schema().dump(command))
       self.db_session.add(instance)
       self.db_session.commit()
       return instance

    def get_book_by_author_and_title(self, author, title):
        return self.db_session.query(Book).filter_by(author=author, title=title).first()
