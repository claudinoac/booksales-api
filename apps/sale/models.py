from sqlalchemy import Column, Float, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from apps.book.models import Book
from apps.customer.models import Customer
from settings.base import DATABASE

book_sale_association = Table(
    "sale_book_sale",
    DATABASE.metadata,
    Column("sale_id", Integer, ForeignKey("sale_sale.id"), nullable=False),
    Column("book_id", Integer, ForeignKey("book_book.id"), nullable=False),
)


class Sale(DATABASE.Model):
    __tablename__ = "sale_sale"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer_customer.id"), nullable=False)
    customer = relationship(Customer, back_populates="sales")
    books = relationship(Book, secondary=book_sale_association, backref="book_sales")
    total_value = Column("total_value", Float(asdecimal=True), default=0)
    charged_value = Column("charged_value", Float(asdecimal=True), default=0)
    applied_discount = Column("applied_discount", Integer, default=0)

    def __repr__(self):
        return f"{self.id} - {self.customer.id}"
