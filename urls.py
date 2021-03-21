from book.urls import routes as book_routes
from tornado.web import url
from base.views import NotFoundView

routes = [
    *book_routes,
    url(r'(.*)', NotFoundView)
]
