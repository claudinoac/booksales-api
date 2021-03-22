from sale.repository import SaleRepository
from customer.repository import CustomerRepository
from book.repository import BookRepository


class SaleValidator:
    command = None

    def __init__(self, command, session):
        self.command = command
        self.repository = SaleRepository(session)
        self.customer_repository = CustomerRepository(session)
        self.book_repository = BookRepository(session)

    def validate(self):
        errors = {}
        errors.update(self.validate_customer())
        errors.update(self.validate_books())
        return errors

        return {}

    def validate_books(self):
        errors = {}
        books = self.book_repository.get_books_by_id_list(self.command.books)
        result_id_list = [book.id for book in books]
        for book_id in self.command.books:
            if book_id not in result_id_list:
                errors.update({
                    f"book_{book_id}_invalid": f"Book with id {book_id} does not exist"
                })

        return errors

    def validate_customer(self):
        customer = self.customer_repository.get_customer_by_id(self.command.customer)
        if not customer:
            return {
                "customer": "The customer with id {} does not exist.".format(self.command.customer)
            }
        return {}
