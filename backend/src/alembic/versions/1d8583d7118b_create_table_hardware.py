"""create table hardware

Revision ID: 1d8583d7118b
Revises: 
Create Date: 2023-03-28 11:34:47.958109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum


# revision identifiers, used by Alembic.
revision = '1d8583d7118b'
down_revision = None
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table(
        'hardwares',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=True),
        sa.Column('amount', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table("hardwares")