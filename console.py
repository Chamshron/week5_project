import pdb
from models.team import Team
from models.player import Player
from models.match import Match

import repositories.team_repository as team_repository
import repositories.player_repository as player_repository
import repositories.match_repository as match_repository

match_repository.delete_all()
player_repository.delete_all()
team_repository.delete_all()

#Team Repository Tests
team1 = Team("Yorkshire Roses", "United Kingdom", 0, [])
team_repository.save(team1)
team2 = Team("Parisian Panthers", "France",0, [])
team_repository.save(team2)
team3 = Team("Steam Rolling Poland", "Poland", 0, [])
team_repository.save(team3)

#Team Repository Tests
# results0 = team_repository.select_all_teams()
# results1 = team_repository.select_one_team(1)
# team_repository.delete_one(1)
# results2 = team_repository.select_all_teams()

#Player Repository Tests
player1 = Player("Kanako Hirai", 2, team1)
player_repository.save_player(player1)
player2 = Player("Ginjing Ching", 4, team1)
player_repository.save_player(player2)
player3 = Player("Emily Flora Knight", 5,team1)
player_repository.save_player(player3)

player4 = Player("Saya Guadarrama", 3,team2)
player_repository.save_player(player4)
player5 = Player("Minh Ha Nguyen", 4, team2)
player_repository.save_player(player5)
player6 = Player("Coralie Texier", 5, team2)
player_repository.save_player(player6)

player7 = Player("Maria Anna Bober", 5,team3)
player_repository.save_player(player7)
player8 = Player("Joanna Labak", 5,team3)
player_repository.save_player(player8)
player9 = Player("Natalia Maj", 5,team3)
player_repository.save_player(player9)

#Player Repository Tests
# player_results0 = player_repository.select_all_players()
# player_results1 = player_repository.select_one_player(1)
# player_repository.delete_one(2)
# player_results2 = player_repository.select_all_players()

#Match Repository Tests
match1 = Match(team1, team2, 1, 0, "Saturday 25th August")
match_repository.save_match(match1)
# pdb.set_trace()
match2 = Match(team1, team3, 2, 2, "Sunday 26th August")
match_repository.save_match(match2)
match3 = Match(team3, team2, 2, 3, "Monday 27th August")
match_repository.save_match(match3)

# #Match Repository Tests
# match01 = match_repository.select_all_matches()
# match02 = match_repository.select_one_match(1)
# match_repository.delete_one(0)
# match03 = match_repository.select_all_matches()

#testing teams for match/match for teams
# result05 = team_repository.teams_for_match(match1)
# result06 = match_repository.matches_for_team(team1)
pdb.set_trace()