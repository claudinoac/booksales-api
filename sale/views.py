from base.views import BaseInstanceView, BaseListView
from sale.models import Sale
from sale.serializers import SaleSerializer


class SaleInstanceView(BaseInstanceView):
    serializer_class = SaleSerializer
    model = Sale


class SaleListView(BaseListView):
    serializer_class = SaleSerializer
    model = Sale
