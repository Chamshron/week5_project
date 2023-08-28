from db.run_sql import run_sql
from models.team import Team
from models.player import Player
from models.match import Match
import pdb

def save(team):
    sql = "INSERT INTO teams(name) VALUES (%s) RETURNING id"
    values = [team.name]
    results = run_sql(sql, values)
    team.id = results[0]['id']
    return team

def select_all_teams():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row['name'], row['country'], row['score'], row['id'])
        teams.append(team)
    return teams 

def select_one_team(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        team = Team(result['name'], result['country'], result['score'],result['players'], result['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, country, score, players, id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.country, team.score, team.players, team.id]
    run_sql(sql,values)

def teams_for_match(match):
    # pdb.set_trace()
    teams = []
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [match.id]
    results = run_sql(sql, values)
    # pdb.set_trace()

    team_a = select_one_team(results[0]['team_a'])
    teams.append(team_a)
    team_b = select_one_team(results[0]['team_b'])
    teams.append(team_b)

    return teams
    

