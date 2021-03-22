from apps.base.handlers import BaseModelCreateHandler
from apps.book.exceptions import BookValidationError
from apps.book.repository import BookRepository
from apps.book.serializers import BookSerializer
from apps.book.validators import BookValidator


class CreateBookHandler(BaseModelCreateHandler):
    serializer_class = BookSerializer
    validator_class = BookValidator
    repository_class = BookRepository
    validation_exception = BookValidationError
