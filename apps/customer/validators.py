from apps.customer.repository import CustomerRepository


class CustomerValidator:
    command = None

    def __init__(self, command, session):
        self.command = command
        self.repository = CustomerRepository(session)

    def validate(self):
        errors = {}
        errors.update(self.validate_email())
        return errors

    def validate_email(self):
        """Checks if a customer with the same email exists in the DB"""
        customer = self.repository.get_customer_by_email(self.command.email)
        if customer:
            return {
                "duplicated": "Customer with email {} already exists.".format(
                    self.command.email,
                )
            }
        return {}
