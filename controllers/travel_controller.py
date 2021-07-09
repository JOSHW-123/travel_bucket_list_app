from flask import Flask, render_template, request, redirect
from flask import Blueprint
from werkzeug.utils import redirect
from repositories import city_repository, country_repository
from models. import Task

tasks_blueprint = Blueprint("tasks", __name__)