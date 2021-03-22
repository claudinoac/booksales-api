from apps.base.views import BaseInstanceView, BaseListView, BaseModelCreateView
from apps.sale.serializers import SaleSerializer
from apps.sale.commands import CreateSaleCommand
from apps.sale.handlers import CreateSaleHandler
from apps.sale.repository import SaleRepository


class SaleInstanceView(BaseInstanceView):
    serializer_class = SaleSerializer
    repository_class = SaleRepository


class SaleListView(BaseListView):
    serializer_class = SaleSerializer
    repository_class = SaleRepository


class SaleCreateView(BaseModelCreateView):
    command_dispatcher = CreateSaleCommand
    handler_class = CreateSaleHandler
