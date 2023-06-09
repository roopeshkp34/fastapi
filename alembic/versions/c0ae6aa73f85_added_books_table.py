"""Added books table

Revision ID: c0ae6aa73f85
Revises: 5eb153fa0e60
Create Date: 2023-05-03 10:33:59.691547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ae6aa73f85'
down_revision = '5eb153fa0e60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books'))
    ),
    sa.ForeignKeyConstraint(
        ["user"], ["user.id"], name=op.f('fk_books_user_user')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
