from tornado.web import url
from sale import views

routes = [
    url('/sales', views.SaleListView, name="sale:list"),
    url(r'/sales/([0-9]+)', views.SaleInstanceView, name="sale:instance"),
]
