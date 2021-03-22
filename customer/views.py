from base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from customer.serializers import CustomerSerializer
from customer.handlers import CreateCustomerHandler
from customer.commands import CreateCustomerCommand
from customer.repository import CustomerRepository


class CustomerInstanceView(BaseInstanceView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerListView(BaseListView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerCreateView(BaseModelCreateView):
    command_dispatcher = CreateCustomerCommand
    handler_class = CreateCustomerHandler
