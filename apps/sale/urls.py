from tornado.web import url

from apps.sale import views

routes = [
    url("/sales", views.SaleListView, name="sale:list"),
    url("/sales/new", views.SaleCreateView, name="sale:new"),
    url(r"/sales/([0-9]+)", views.SaleInstanceView, name="sale:instance"),
]
