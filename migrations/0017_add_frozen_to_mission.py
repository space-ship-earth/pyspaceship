"""
add frozen to mission
date created: 2019-05-05 18:42:58.476185
"""

def upgrade(migrator):
  migrator.add_column('mission', 'frozen', 'bool', default=False)
  migrator.execute_sql('update mission set frozen=true;')
  migrator.add_column('mission', 'duration_in_weeks', 'int', default=4)
  migrator.add_column('mission', 'started_at', 'char', null=True)

def downgrade(migrator):
  migrator.drop_column('mission', 'frozen')
  migrator.drop_column('mission', 'duration_in_weeks')
  migrator.drop_column('mission', 'started_at')