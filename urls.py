from book.urls import routes as book_routes
from customer.urls import routes as customer_routes
from tornado.web import url
from base.views import NotFoundView

routes = [
    *book_routes,
    *customer_routes,
    url(r'(.*)', NotFoundView)
]
