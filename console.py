import pdb
from models.team import Team
from models.player import Player
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

team_repository.delete_all
player_repository.delete_all

team1 = Team("Team GB", "United Kingdom", 0)
team_repository.save(team1)
team2 = Team("Team France", "France",0)
team_repository.save(team2)
team3 = Team("Team Poland", "Poland", 0)
team_repository.save(team3)

#Team Repository Tests
# results0 = team_repository.select_all_teams()
# results1 = team_repository.select_one_team(1)
# team_repository.delete_one(1)
# results2 = team_repository.select_all_teams

#Player Repository Tests
# player1 = Player("Kanako Hirai", 2, "Team GB")
# player_repository.save_player(player1)
# player2 = Player("Ginjing Ching", 4, "Team GB")
# player_repository.save_player(player2)
# player3 = Player("Emily Flora Knight", 5,"Team GB")
# player_repository.save_player(player3)
# player_results = player_repository.select_all_players()

pdb.set_trace()