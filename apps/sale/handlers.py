from apps.sale.repository import SaleRepository
from apps.sale.validators import SaleValidator
from apps.sale.exceptions import SaleValidationError
from apps.sale.serializers import SaleSerializer
from apps.base.handlers import BaseModelCreateHandler


class CreateSaleHandler(BaseModelCreateHandler):
    serializer_class = SaleSerializer
    validator_class = SaleValidator
    repository_class = SaleRepository
    validation_exception = SaleValidationError

    def handle(self, command):
        validator = self.validator_class(command, self.db_session)
        errors = validator.validate()
        if not errors:
            repository = self.repository_class(self.db_session)
            created_object = repository.create_object(command)
            serializer = self.serializer_class(created_object)
            return serializer.as_dict()
        raise self.validation_exception(errors)


class GetSaleDiscountHandler:

    def handle(self, command):
        pass
