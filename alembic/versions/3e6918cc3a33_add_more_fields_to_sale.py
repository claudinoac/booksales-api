"""add_more_fields_to_sale

Revision ID: 3e6918cc3a33
Revises: b15f4151276d
Create Date: 2021-03-21 22:13:30.939512

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '3e6918cc3a33'
down_revision = 'b15f4151276d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sale_sale', sa.Column('applied_discount', sa.Integer(), nullable=True))
    op.add_column('sale_sale', sa.Column('charged_value', sa.Float(asdecimal=True), nullable=True))
    op.add_column('sale_sale', sa.Column('total_value', sa.Float(asdecimal=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sale_sale', 'total_value')
    op.drop_column('sale_sale', 'charged_value')
    op.drop_column('sale_sale', 'applied_discount')
    # ### end Alembic commands ###
