"""add last few columns to posts table

Revision ID: 0390be9ce9ab
Revises: 5d088786b47a
Create Date: 2022-05-25 17:49:27.035326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0390be9ce9ab'
down_revision = '5d088786b47a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
