"""add unique email to customer

Revision ID: f3c6f75d2ddb
Revises: 3e6918cc3a33
Create Date: 2021-03-22 01:20:19.511621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3c6f75d2ddb'
down_revision = '3e6918cc3a33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'customer_customer', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer_customer', type_='unique')
    # ### end Alembic commands ###