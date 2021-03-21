from book.repository import BookRepository
from book.validators import BookValidator
from book.exceptions import BookValidationError

class CreateBookHandler:
    db_session = None

    def __init__(self, db_session):
        self.db_session = db_session

    def handle(self, command):
        validator = BookValidator(command, self.db_session)
        errors = validator.validate()
        if not errors:
            repository = BookRepository(self.db_session)
            return repository.create_book(command)
        raise BookValidationError(errors)
