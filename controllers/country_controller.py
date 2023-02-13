from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import city_repository, country_repository
from models.country import Country
from models.city import City


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)

@countries_blueprint.route("/countries/new")
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new.html", all_countries=countries)

@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    geographical_area = request.form["geographical_area"]
    population = request.form["population"]
    language = request.form["language"]
    currency = request.form["currency"]
    visited = request.form["visited"]
    country = Country(name, geographical_area, population, language, currency, visited)
    country_repository.save(country)
    return redirect("/countries")

# Come back to this one, route(redirect) may need to be changed.
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country=country)

@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template("countries/edit.html", country=country,
    all_cities=cities)

# Come back to this one, route(redirect) may need to be changed.
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    geographical_area = request.form["geographical_area"]
    population = request.form["population"]
    language = request.form["language"]
    currency = request.form["currency"]
    visited = request.form['visited']
    country = Country(name, geographical_area, population, language, currency, visited, id)
    country_repository.update(country)
    return redirect("/countries"), 302


    