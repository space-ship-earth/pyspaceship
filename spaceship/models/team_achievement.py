import pendulum
from sqlalchemy.ext.hybrid import hybrid_property

from spaceship.db import db
from spaceship.models.custom_fields import PendulumDateTimeField

class TeamAchievement(db.Model):
  id = db.Column(db.Integer, primary_key=True)

  name = db.Column(db.String(127))

  team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
  team = db.relationship('Team', backref='achievements')

  mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=True)
  mission = db.relationship('Mission', backref='achievements')

  created_at = db.Column(PendulumDateTimeField(), default=lambda: pendulum.now('UTC'))
  deleted_at = db.Column(PendulumDateTimeField(), nullable=True)

  @hybrid_property
  def is_deleted(self):
    return self.deleted_at == None
