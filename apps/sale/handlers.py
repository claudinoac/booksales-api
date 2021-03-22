from apps.base.handlers import BaseModelCreateHandler
from apps.sale.exceptions import SaleValidationError
from apps.sale.repository import SaleRepository
from apps.sale.serializers import SaleSerializer
from apps.sale.validators import SaleValidator


class CreateSaleHandler(BaseModelCreateHandler):
    serializer_class = SaleSerializer
    validator_class = SaleValidator
    repository_class = SaleRepository
    validation_exception = SaleValidationError


class GetSaleDiscountHandler:
    def handle(self, command):
        pass
