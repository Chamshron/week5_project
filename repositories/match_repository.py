from db.run_sql import run_sql
from models.match import Match
from models.team import Team
import pdb

def save_match(match):
    sql = "INSERT INTO matches(team_a, team_b, team_a_score, team_b_score, match_date) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [match.team_a.id, match.team_b.id, match.team_a_score, match.team_b_score, match.match_date]
    results = run_sql(sql, values)
    # pdb.set_trace()
    match.id = results[0]['id']
    return match

def select_all_matches():
    matches = []
    sql = "SELECT * FROM matches"
    results = run_sql(sql)
    for row in results:
        match = Match(row['team_a'], row['team_b'], row['team_a_score'], row['team_b_score'], row['match_date'], row['id'])
        matches.append(match)
    return matches

def select_one_match(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['team_a'], result['team_b'], result['team_a_score'], result['team_b_score'], result['match_date'], result['id'])
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(match):
    sql = "UPDATE matches SET (team_a, team_b, match_date, id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [match.team_a, match.team_b, match.team_a_score, match.team_b_score, match.match_date, match.id]
    run_sql(sql, values)

def matches_for_team(team):
    matches = []
    # pdb.set_trace()
    sql = "SELECT * FROM matches WHERE team_a = %s OR team_b = %s"
    values = [team.id,team.id]
    results = run_sql(sql, values)
    for row in results:
        match = select_one_match(row['id'])
        matches.append(match)
    return matches
