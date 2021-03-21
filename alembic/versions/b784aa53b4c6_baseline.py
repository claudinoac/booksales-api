"""baseline

Revision ID: b784aa53b4c6
Revises:
Create Date: 2021-03-20 19:52:24.769161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b784aa53b4c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_book',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(250)),
        sa.Column('year', sa.SmallInteger),
        sa.Column('price', sa.Float(asdecimal=True)),
        sa.Column('author', sa.String(250)),
        sa.Column('ISBN', sa.BigInteger),
        sa.Column('language', sa.String(250))
    )


def downgrade():
    op.drop_table('book_book')
