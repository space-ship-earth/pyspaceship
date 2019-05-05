"""
drop mission_started_at from team
date created: 2019-05-05 19:10:41.028519
"""
from peewee import CharField

def upgrade(migrator):
  migrator.drop_column('team', 'mission_start_at')

def downgrade(migrator):
  migrator.add_column('team', 'mission_start_at', CharField, null=True)
