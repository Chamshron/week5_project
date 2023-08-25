import pdb
from models.team import Team
import repositories.team_repository as team_repository

team1 = Team("Team GB", "United Kingdom", 0)
team_repository.save(team1)
team2 = Team("Team France", "France",0)
team_repository.save(team2)
team3 = Team("Team Poland", "Poland", 0)
team_repository.save(team3)

results = team_repository.select_all_teams()
pdb.set_trace()