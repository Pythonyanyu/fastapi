"""add content column to posts table

Revision ID: 9a62e8c79d1d
Revises: 446260fea61a
Create Date: 2022-05-25 17:27:14.967911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a62e8c79d1d'
down_revision = '446260fea61a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
