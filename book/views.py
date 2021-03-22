from base.views import BaseInstanceView, BaseListView
from book.models import Book
from book.serializers import BookSerializer
from book.commands import CreateBookCommand
from book.handlers import CreateBookHandler
from base.views import BaseModelCreateView
from book.repository import BookRepository


class BookInstanceView(BaseInstanceView):
    serializer_class = BookSerializer
    model = Book
    repository_class = BookRepository


class BookListView(BaseListView):
    serializer_class = BookSerializer
    repository_class = BookRepository
    model = Book


class BookCreateView(BaseModelCreateView):
    command_dispatcher = CreateBookCommand
    handler_class = CreateBookHandler
