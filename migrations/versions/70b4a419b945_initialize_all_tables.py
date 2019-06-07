"""initialize all tables

Revision ID: 70b4a419b945
Revises:
Create Date: 2019-06-06 17:29:20.296155

"""
from alembic import op
import sqlalchemy as sa
import spaceship


# revision identifiers, used by Alembic.
revision = '70b4a419b945'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # drop all tables to start
    conn = op.get_bind()
    conn.execute('set FOREIGN_KEY_CHECKS=0')
    for t in ['migration_history', 'team_achievement', 'mission_goal', 'mission', 'invitation', 'user_achievement', 'team_user', 'team', 'goal', 'user']:
      try:
        op.drop_table(t)
      except:
        pass
    conn.execute('set FOREIGN_KEY_CHECKS=1')

    # now let alembic re-create them
    op.create_table('goal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('category', sa.String(length=127), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=127), nullable=True),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('password_hash', sa.String(length=127), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('captain_id', sa.Integer(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['captain_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'team_id')
    )
    op.create_table('user_achievement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invitation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key_for_sharing', sa.String(length=40), nullable=False),
    sa.Column('inviter_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('invited_email', sa.String(length=127), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=127), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['inviter_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key_for_sharing')
    )
    op.create_table('mission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=127), nullable=True),
    sa.Column('short_description', sa.String(length=127), nullable=True),
    sa.Column('duration_in_weeks', sa.SmallInteger(), nullable=True),
    sa.Column('frozen', sa.Boolean(), nullable=True),
    sa.Column('started_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mission_goal',
    sa.Column('mission_id', sa.Integer(), nullable=False),
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('week', sa.SmallInteger(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.id'], ),
    sa.ForeignKeyConstraint(['mission_id'], ['mission.id'], ),
    sa.PrimaryKeyConstraint('mission_id', 'goal_id')
    )
    op.create_table('team_achievement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('mission_id', sa.Integer(), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['mission_id'], ['mission.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_achievement')
    op.drop_table('mission_goal')
    op.drop_table('mission')
    op.drop_table('invitation')
    op.drop_table('user_achievement')
    op.drop_table('team_user')
    op.drop_table('team')
    op.drop_table('user')
    op.drop_table('goal')
    # ### end Alembic commands ###
