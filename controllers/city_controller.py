from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import city_repository, country_repository
from models.city import City
from models.country import Country

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("/cities/index.html", all_cities=cities)

@cities_blueprint.route("/cities/new")
def new_city():
    cities = city_repository.select_all()
    return render_template("cities/new.html", all_cities=cities)

# Revisit this one, something doesn't look right.
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    country = country_repository.select(request.form["country_id"])
    attractions = request.form["attractions"]
    temperature = request.form["temperature"]
    visited = request.form["visited"]
    city = City(name, country, attractions, temperature, id, visited)
    city_repository.save(city)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>", methods=["GET"])
def show_city(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city=city)

@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city=city,
    all_countries=countries)

@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    name = request.form["name"]
    country = country_repository.select(request.form["country_id"])
    attractions = request.form["attractions"]
    temperature = request.form["temperature"]
    visited = request.form["visited"]
    city = City(name, country, attractions, temperature, id, visited)
    city_repository.update(city)
    return redirect("/cities")


        # self.name = name
        # self.country = country
        # self.attractions = attractions
        # self.temperature = temperature
        # self.id = id
        # self.visited = visited