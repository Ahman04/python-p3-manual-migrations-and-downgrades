"""Rename name to full_name

Revision ID: bf9d97956e70
Revises: 394201deb313
Create Date: 2025-12-05 15:44:08.647409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf9d97956e70'
down_revision = '394201deb313'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade():
    op.alter_column('students', 'full_name', new_column_name='name')
