"""create table reserve

Revision ID: 062eb59b1cfb
Revises: 1d8583d7118b
Create Date: 2023-03-28 11:35:26.594321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '062eb59b1cfb'
down_revision = '1d8583d7118b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'reserves',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hardware_id', sa.Integer(), nullable=False),
        sa.Column('name_teacher', sa.String(length=200), nullable=False),
        sa.Column('loan_date', sa.Date(), nullable=False),
        sa.Column('return_date', sa.Date(), nullable=False),
        sa.Column('comments', sa.String(length=200), nullable=True),
        sa.ForeignKeyConstraint(['hardware_id'], ['hardware.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('reserves')