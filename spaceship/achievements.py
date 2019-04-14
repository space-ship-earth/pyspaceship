from .models.user import User
from .models.team import Team
from .models.team_achievement import TeamAchievement
from .models.user_achievement import UserAchievement

kinds = {}

class Achievement(object):
  '''Something praiseworthy a user or team does (base class).'''
  def __init__(self, name='', short_description='', **kwargs):
    self.name = name
    self.short_description = short_description
    self.badge_url = kwargs.get('badge_url', '')
    self.is_team = kwargs.get('is_team', False)
    kinds[name] = self

  def __call__(self, model):
    if self.is_team:
      ta = TeamAchievement(team_id=model.id, name=self.name)
      ta.save()
      return

    ua = UserAchievement(user_id=model.id, name=self.name)
    ua.save()


# miscellaneous placeholder for unknown achievements from db
unknown_achievement = Achievement(
  name='Good job',
  short_description='You did something'
)

# real achievements
pledge_for_goal = Achievement(
  name='Pledge for a goal',
  short_description='Awarded for completing the Plant based diet mission'
)

fulfill_pledge = Achievement(
  name='Fulfill a pledge',
  short_description='Awarded for fulfilling a pledge'
)

become_captain = Achievement(
  name='Become a captain',
  short_description='Awarded for becoming a captain'
)

invite_crew = Achievement(
  name='Invite crew',
  short_description='Awarded for inviting crew to join'
)

start_mission = Achievement(
  name='Start mission',
  short_description='Awarded for starting a mission',
  is_team=True
)


class CompleteMissionAchievement(Achievement):
  '''Records which mission and specializes display based on it.'''

  def __init__(self):
    super().__init__(name='Complete mission',
                     short_description='Awarded for completing a mission')

  def __call__(self, team, mission):
    ta = TeamAchievement(team=team, name=self.name)
    ta.mission_completed = mission
    ta.save()


complete_mission = CompleteMissionAchievement()

def for_user(user):
  return [kinds.get(ua.name, unknown_achievement)
          for ua in user.achievements]

def for_team(team):
  return [kinds.get(ta.name, unknown_achievement)
          for ta in team.achievements]