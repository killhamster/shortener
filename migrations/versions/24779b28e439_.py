"""empty message

Revision ID: 24779b28e439
Revises: 
Create Date: 2022-05-18 15:14:55.460675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24779b28e439'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=500), nullable=False),
    sa.Column('short_id', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_urls')
    # ### end Alembic commands ###
