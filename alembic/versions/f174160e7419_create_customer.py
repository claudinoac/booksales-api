"""baseline

Revision ID: f174160e7419
Revises:
Create Date: 2021-03-20 19:52:24.769161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f174160e7419'
down_revision = '8b7e0f3cc210'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer_customer',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('first_name', sa.String(250), nullable=False),
        sa.Column('last_name', sa.String(250), nullable=False),
        sa.Column('email', sa.String(250), nullable=False),
        sa.Column('phone', sa.String(20), nullable=False)
    )


def downgrade():
    op.drop_table('customer_customer')
