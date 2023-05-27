"""remove name from renter details

Revision ID: 8218a84949e2
Revises: 237cdd13b8ef
Create Date: 2022-12-08 12:11:03.989169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8218a84949e2'
down_revision = '237cdd13b8ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('instrumentrenterdetails', 'renterName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instrumentrenterdetails', sa.Column('renterName', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    # ### end Alembic commands ###