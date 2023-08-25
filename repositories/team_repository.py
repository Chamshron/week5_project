from db.run_sql import run_sql
from models.team import Team

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