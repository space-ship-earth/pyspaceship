"""create missing tables

Revision ID: 7d648ddc717b
Revises: 70b4a419b945
Create Date: 2019-06-20 17:44:33.049212

"""
from alembic import op
import sqlalchemy as sa
import spaceship

# revision identifiers, used by Alembic.
revision = '7d648ddc717b'
down_revision = '70b4a419b945'
branch_labels = None
depends_on = None


def upgrade():
    # these might already exist in some environments
    for t in ['pledge', 'achievement']:
      try:
        op.drop_table(t)
      except:
        pass

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('badge_url', sa.String(length=256), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pledge',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mission_id', sa.Integer(), nullable=False),
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('fulfilled', sa.Boolean(), nullable=True),
    sa.Column('start_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('end_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.id'], ),
    sa.ForeignKeyConstraint(['mission_id'], ['mission.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'mission_id', 'goal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pledge')
    op.drop_table('achievement')
    # ### end Alembic commands ###