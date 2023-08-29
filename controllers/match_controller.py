from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.match import Match

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all_matches()
    return render_template ("matches/index.html", matches=matches)

@matches_blueprint.route("/matches/<id>")
def show(id):
    match = match_repository.select_one_match(id)
    return render_template("matches/show.html", match = match)

@matches_blueprint.route("/matches/new", methods = ['GET'])
def new_match():
    matches = match_repository.select_all_matches()
    teams = team_repository.select_all_teams()
    return render_template("matches/new.html", matches = matches, teams=teams)

@matches_blueprint.route("/matches", methods=['POST'])
def create_match():
    teams = team_repository.select_all_teams()
    team_a = team_repository.select_one_team(request.form['team_a'])
    team_b = team_repository.select_one_team(request.form['team_b'])
    team_a_score = request.form['team_a_score']
    team_b_score = request.form['team_b_score']
    match_date = request.form['match_date']
    match = Match(team_a, team_b, team_a_score, team_b_score, match_date)
    match_repository.save_match(match)
    return redirect("/matches")

@matches_blueprint.route("/matches/<id>/edit", methods=['GET'])
def match(id):
    match = match_repository.select_one_match(id)
    return render_template('matches/edit.html', match = match)

@matches_blueprint.route("/matches/<id>/delete", methods = ['POST'])
def delete_match(id):
    match_repository.delete_one(id)
    return redirect('/matches')
