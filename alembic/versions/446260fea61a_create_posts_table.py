"""create posts table

Revision ID: 446260fea61a
Revises: 89d51fbff9b1
Create Date: 2022-05-25 16:53:11.737308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '446260fea61a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
