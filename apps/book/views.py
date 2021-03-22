from apps.base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from apps.book.commands import CreateBookCommand
from apps.book.handlers import CreateBookHandler
from apps.book.models import Book
from apps.book.repository import BookRepository
from apps.book.serializers import BookSerializer


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
