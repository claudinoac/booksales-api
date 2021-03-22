from sale.models import Sale
from base.repository import BaseRepository
from book.repository import BookRepository
from decimal import Decimal
from sqlalchemy.sql import func


class SaleRepository(BaseRepository):
    model = Sale

    def __init__(self, db_session):
        self.db_session = db_session
        self.book_repository = BookRepository(self.db_session)

    def get_discount_for_customer(self, customer_id):
        total_sales_amount = self.db_session.query(
            func.sum(Sale.total_value)
        ).filter(Sale.customer_id == customer_id).scalar() or Decimal(0)

        if total_sales_amount > Decimal(1000):
            if total_sales_amount > Decimal(5000):
                if total_sales_amount > Decimal(15000):
                    return 20
                return 15
            return 10
        return 0

    def create_object(self, command):
        discount = self.get_discount_for_customer(command.customer)
        new_sale = Sale(
            customer_id=command.customer
        )
        book_list = self.book_repository.get_books_by_id_list(command.books)
        new_sale.books.extend(book_list)

        new_sale.total_value = sum([book.price for book in book_list])
        if discount:
            new_sale.charged_value = new_sale.total_value * Decimal((1 - discount/100))
            new_sale.applied_discount = discount
        else:
            new_sale.charged_value = new_sale.total_value

        self.db_session.add(new_sale)
        self.db_session.commit()
        return new_sale
