from db.run_sql import run_sql
from models.player import Player
import repositories.team_repository as team_repositories

def save_player(player):
    sql = "INSERT INTO players(name, grade, team) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.grade, player.team]
    results = run_sql(sql, values)
    player.id = results[0]['id']
    return player

def select_all_players():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['name'], row['grade'], row['team'], row['id'])
        players.append(player)
    return players

def select_one_player(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = team_repositories.select_one_team(result['team'])
        player = Player(result['name'], result['grade'], team, result['id'])
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(player):
    sql = "UPDATE players SET (name, grade, team, id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.grade, player.team,player.id]
    results = run_sql(sql, values)