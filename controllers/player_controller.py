from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository 

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all_players()
    return render_template ("players/index.html", players=players)

@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select_one_player(id)
    return render_template("players/show.html", player = player)