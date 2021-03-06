from tornado.web import url

from apps.base.views import NotFoundView
from apps.book.urls import routes as book_routes
from apps.book.views import BookListView
from apps.customer.urls import routes as customer_routes
from apps.sale.urls import routes as sale_routes

routes = [
    *book_routes,
    *customer_routes,
    *sale_routes,
    url("/", BookListView, name="default-view"),
    url(r"(.*)", NotFoundView),
]
