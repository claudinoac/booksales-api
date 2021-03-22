from apps.customer.repository import CustomerRepository
from apps.customer.validators import CustomerValidator
from apps.customer.exceptions import CustomerValidationError
from apps.customer.serializers import CustomerSerializer
from apps.base.handlers import BaseModelCreateHandler


class CreateCustomerHandler(BaseModelCreateHandler):
    serializer_class = CustomerSerializer
    validator_class = CustomerValidator
    repository_class = CustomerRepository
    validation_exception = CustomerValidationError
