from book.repository import BookRepository
from book.validators import BookValidator
from book.exceptions import BookValidationError
from book.serializers import BookSerializer
from base.handlers import BaseModelCreateHandler


class CreateBookHandler(BaseModelCreateHandler):
    serializer_class = BookSerializer
    validator_class = BookValidator
    repository_class = BookRepository
    validation_exception = BookValidationError
