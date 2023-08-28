from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all_matches()
    return render_template ("matches/index.html", matches=matches)

@matches_blueprint.route("/matches/<id>")
def show(id):
    match = match_repository.select_one_match(id)
    return render_template("matches/show.html", match = match)