from base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from sale.serializers import SaleSerializer
from sale.commands import CreateSaleCommand
from sale.handlers import CreateSaleHandler
from sale.repository import SaleRepository


class SaleInstanceView(BaseInstanceView):
    serializer_class = SaleSerializer
    repository_class = SaleRepository


class SaleListView(BaseListView):
    serializer_class = SaleSerializer
    repository_class = SaleRepository


class SaleCreateView(BaseModelCreateView):
    command_dispatcher = CreateSaleCommand
    handler_class = CreateSaleHandler
