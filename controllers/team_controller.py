from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.team import Team

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all_teams()
    return render_template ("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select_one_team(id)
    return render_template("teams/show.html", team = team)

@teams_blueprint.route("/teams/new", methods=['GET'])
def new_task():
    teams = team_repository.select_all_teams()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    name = request.form['name']
    country = request.form['country']
    score = request.form['score']
    players = request.form['players']
    id = request.form['id']
    team = Team(name, country, score, players, id)
    team_repository.save(team)
    return redirect("/teams")
    