from tornado.web import url
from apps.customer import views

routes = [
    url('/customers', views.CustomerListView, name="customer:list"),
    url('/customers/new', views.CustomerCreateView, name="customer:create"),
    url(r'/customers/([0-9]+)', views.CustomerInstanceView, name="customer:instance"),
]
