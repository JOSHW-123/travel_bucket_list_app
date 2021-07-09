from flask import Flask, render_template, request, redirect
from flask import Blueprint
from werkzeug.utils import redirect
from repositories import city_repository, country_repository
from models.country import Country
from models.city import City


countries_blueprint = Blueprint("countries", __name__)