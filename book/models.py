from settings.development import DATABASE
from sqlalchemy import Column, BigInteger, Integer, String, Float, SmallInteger
from sqlalchemy.orm import validates


class Book(DATABASE.Model):
    __tablename__ = "book_book"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(250), nullable=False)
    year = Column('year', SmallInteger, nullable=False)
    price = Column('price', Float(asdecimal=True), nullable=False)
    author = Column('author', String(250), nullable=False)
    ISBN = Column('ISBN', BigInteger, nullable=False)
    language = Column('language', String(250), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.title}"