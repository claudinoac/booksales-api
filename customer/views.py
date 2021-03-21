from base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from customer.models import Customer
from customer.serializers import CustomerSerializer
from customer.handlers import CreateCustomerHandler
from customer.commands import CreateCustomerCommand


class CustomerInstanceView(BaseInstanceView):
    serializer_class = CustomerSerializer
    model = Customer


class CustomerListView(BaseListView):
    serializer_class = CustomerSerializer
    model = Customer


class CustomerCreateView(BaseModelCreateView):
    command_dispatcher = CreateCustomerCommand
    handler_class = CreateCustomerHandler
