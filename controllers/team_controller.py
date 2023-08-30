from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.team import Team
from models.match import Match
import pdb

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all_teams()
    # pdb.set_trace()
    return render_template ("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select_one_team(id)
    matches = match_repository.matches_for_team(team)
    return render_template("teams/show.html", team = team, matches=matches)

@teams_blueprint.route("/teams/new", methods=['GET'])
def new_task():
    teams = team_repository.select_all_teams()
    return render_template("teams/new.html", teams=teams)

@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    name = request.form['name']
    country = request.form['country']
    score = request.form['score']
    team = Team(name, country, score, id)
    team_repository.save(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = team_repository.select_one_team(id)
    return render_template('teams/edit.html', team = team)

@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    name = request.form['name']
    country = request.form['country']
    score = request.form['score']
    team = Team(name, country, score, id)
    team_repository.update(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods = ['POST'])
def delete_team(id):
    team_repository.delete_one(id)
    return redirect('/teams')

    