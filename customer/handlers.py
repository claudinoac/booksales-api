from customer.repository import CustomerRepository
from customer.validators import CustomerValidator
from customer.exceptions import CustomerValidationError
from customer.serializers import CustomerSerializer
from base.handlers import BaseModelCreateHandler


class CreateCustomerHandler(BaseModelCreateHandler):
    serializer_class = CustomerSerializer
    validator_class = CustomerValidator
    repository_class = CustomerRepository
    validation_exception = CustomerValidationError
