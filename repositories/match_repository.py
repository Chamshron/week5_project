from db.run_sql import run_sql
from models.match import Match

def save_match(match):
    sql = "INSERT INTO matches(match_date) VALUES (%s) RETURNING id"
    values = [match.match_date]
    results = run_sql(sql, values)
    match.id = results[0]['id']
    return match

def select_all_matches():
    matches = []
    sql = "SELECT * FROM matches"
    results = run_sql(sql)
    for row in results:
        match = Match(row['team_a'], row['team_b'], row['match_date'], row['id'])
        matches.append(match)
    return matches

def select_one_match(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['team_a'], result['team_b'], result['match_date'], result['id'])
    return match

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)