from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository 
from models.player import Player

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all_players()
    return render_template ("players/index.html", players=players)

@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select_one_player(id)
    return render_template("players/show.html", player = player)

@players_blueprint.route("/players/new", methods=['GET'])
def new_player():
    players = player_repository.select_all_players()
    teams = team_repository.select_all_teams()
    return render_template("players/new.html", players=players, teams=teams)

@players_blueprint.route("/players", methods=['POST'])
def create_a_player():
    teams = team_repository.select_all_teams()
    name = request.form['name']
    grade = request.form['grade']
    team = team_repository.select_one_team(request.form['team'])
    player = Player(name, grade, team)
    player_repository.save_player(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/delete", methods = ['POST'])
def delete_player(id):
    player_repository.delete_one(id)
    return redirect('/players')

