from apps.base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from apps.customer.serializers import CustomerSerializer
from apps.customer.handlers import CreateCustomerHandler
from apps.customer.commands import CreateCustomerCommand
from apps.customer.repository import CustomerRepository


class CustomerInstanceView(BaseInstanceView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerListView(BaseListView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerCreateView(BaseModelCreateView):
    command_dispatcher = CreateCustomerCommand
    handler_class = CreateCustomerHandler
