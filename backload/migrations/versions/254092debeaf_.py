"""empty message

Revision ID: 254092debeaf
Revises: c016409a7b8b
Create Date: 2020-01-28 16:59:57.391121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254092debeaf'
down_revision = 'c016409a7b8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('master', sa.Column('sku', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('master', 'sku')
    # ### end Alembic commands ###
