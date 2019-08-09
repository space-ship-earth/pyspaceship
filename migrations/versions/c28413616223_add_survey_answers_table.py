"""add-survey-answers-table

Revision ID: c28413616223
Revises: 04e26d6557e7
Create Date: 2019-08-08 20:53:40.634560

"""
from alembic import op
import sqlalchemy as sa
import spaceship

# revision identifiers, used by Alembic.
revision = 'c28413616223'
down_revision = '04e26d6557e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey_answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mission_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('survey_version', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.String(length=5), nullable=True),
    sa.Column('answer', sa.String(length=256), nullable=True),
    sa.Column('created_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.Column('deleted_at', spaceship.models.custom_fields.PendulumDateTimeField(), nullable=True),
    sa.ForeignKeyConstraint(['mission_id'], ['mission.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'mission_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('survey_answer')
    # ### end Alembic commands ###
