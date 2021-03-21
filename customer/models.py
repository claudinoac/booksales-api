from settings.development import DATABASE
from sqlalchemy import Column, Integer, String

class Customer(DATABASE.Model):
    __tablename__ = "customer_customer"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(250), nullable=False)
    last_name = Column('last_name', String(250), nullable=False)
    email = Column('email', String(250), nullable=False)
    phone = Column('phone', String(20), nullable=False)

    def __repr__(self):
        return f"{self.id - self.email}"
