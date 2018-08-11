"""created workout schema and workout

Revision ID: d31d468ab947
Revises: 57cb702b7630
Create Date: 2018-08-11 13:07:27.841366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd31d468ab947'
down_revision = '57cb702b7630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE SCHEMA workout')
    op.create_table('workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('ts_start', sa.DateTime(), nullable=False),
    sa.Column('ts_finish', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['master.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='workout'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout', schema='workout')
    op.execute('DROP SCHEMA workout')
    # ### end Alembic commands ###
