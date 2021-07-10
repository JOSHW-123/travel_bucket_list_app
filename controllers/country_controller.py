from flask import Flask, render_template, request, redirect
from flask import Blueprint
from werkzeug.utils import redirect
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

@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country=country)

    # self.name = name
    #     self.geographical_area = geographical_area
    #     self.population = population
    #     self.language = language
    #     self.currency = currency
    #     self.id = id
    #     self.visited = visited


# @tasks_blueprint.route("/tasks")
# def tasks():
#     tasks = task_repository.select_all()
#     return render_template("tasks/index.html", all_tasks=tasks)

# @tasks_blueprint.route("/tasks/new")
# def new_task():
#     users = user_repository.select_all()
#     return render_template("tasks/new.html", all_users=users)

# @tasks_blueprint.route("/tasks", methods=["POST"])
# def create_task():
#     description = request.form["description"]
#     duration = request.form["duration"]
#     completed = request.form["completed"]
#     user_id = request.form["user_id"]
#     user = user_repository.select(user_id)
#     new_task = Task(description, user, duration, completed)
#     task_repository.save(new_task)
#     return redirect("/tasks")


# # @tasks_blueprint.route("/tasks", methods=["POST"])
# # def create_task():
# #     print(request.form)
# # This will show immutable object in terminal

# @tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
# def delete_task(id):
#     task_repository.delete(id)
#     return redirect("/tasks")

# @tasks_blueprint.route("/tasks/<id>", methods=["GET"])
# def show_task(id):
#     task = task_repository.select(id)
#     return render_template("tasks/show.html", task = task)

# @tasks_blueprint.route("/tasks/<id>/edit", methods=["GET"])
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template("tasks/edit.html", task = task,
#     all_users = users)

# @tasks_blueprint.route("/tasks/<id>", methods=['POST'])
# def update_task(id):
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed, id)
#     task_repository.update(task)
#     return redirect('/tasks')
