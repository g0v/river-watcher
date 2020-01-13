"""empty message

Revision ID: 860005cd2962
Revises: 31ba749043d9
Create Date: 2019-12-05 12:04:21.611117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '860005cd2962'
down_revision = '31ba749043d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('time_updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'time_updated')
    # ### end Alembic commands ###
