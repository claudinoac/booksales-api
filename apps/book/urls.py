from tornado.web import url
from apps.book import views

routes = [
    url('/books', views.BookListView, name="book:list"),
    url('/books/new', views.BookCreateView, name="book:create"),
    url(r'/books/([0-9]+)', views.BookInstanceView, name="book:instance"),
]
