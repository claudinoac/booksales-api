from tornado.web import url
from book import views

routes = [
    url('/books', views.BookListView, name="book:list"),
    url(r'/books/([0-9]+)', views.BookInstanceView, name="book:instance"),
]
