from apps.base.repository import BaseRepository
from apps.customer.models import Customer


class CustomerRepository(BaseRepository):
    model = Customer

    def get_customer_by_email(self, email):
        return self.db_session.query(self.model).filter_by(email=email).first()

    def get_customer_by_id(self, customer_id):
        return self.db_session.query(self.model).filter_by(id=customer_id).first()
