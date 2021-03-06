"""empty message

Revision ID: ba1adcccbb6b
Revises: None
Create Date: 2016-07-31 11:38:31.078543

"""

# revision identifiers, used by Alembic.
revision = 'ba1adcccbb6b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    ### end Alembic commands ###
