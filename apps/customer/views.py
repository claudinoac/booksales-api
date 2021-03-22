from apps.base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from apps.customer.commands import CreateCustomerCommand
from apps.customer.handlers import CreateCustomerHandler
from apps.customer.repository import CustomerRepository
from apps.customer.serializers import CustomerSerializer


class CustomerInstanceView(BaseInstanceView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerListView(BaseListView):
    serializer_class = CustomerSerializer
    repository_class = CustomerRepository


class CustomerCreateView(BaseModelCreateView):
    command_dispatcher = CreateCustomerCommand
    handler_class = CreateCustomerHandler
