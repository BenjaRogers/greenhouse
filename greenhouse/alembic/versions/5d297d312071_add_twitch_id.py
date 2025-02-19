"""Add twitch id

Revision ID: 5d297d312071
Revises: 778d6aa05318
Create Date: 2023-02-13 13:34:59.629026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d297d312071'
down_revision = '778d6aa05318'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('twitch_id', sa.String(length=12), nullable=False))
    op.create_unique_constraint(None, 'users', ['twitch_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'twitch_id')
    # ### end Alembic commands ###
