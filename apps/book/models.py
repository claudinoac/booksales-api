from sqlalchemy import BigInteger, Column, Float, Integer, SmallInteger, String, UniqueConstraint

from settings.base import DATABASE


class Book(DATABASE.Model):
    __tablename__ = "book_book"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(250), nullable=False)
    year = Column("year", SmallInteger, nullable=False)
    price = Column("price", Float(asdecimal=True), nullable=False)
    author = Column("author", String(250), nullable=False)
    ISBN = Column("ISBN", BigInteger, nullable=False, unique=True)
    language = Column("language", String(250), nullable=False)
    UniqueConstraint("title", "author", name="title_author")

    def __repr__(self):
        return f"{self.id} - {self.title}"
