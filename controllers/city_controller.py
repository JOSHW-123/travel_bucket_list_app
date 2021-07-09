from flask import Flask, render_template, request, redirect
from flask import Blueprint
from werkzeug.utils import redirect
from repositories import city_repository, country_repository
from models.city import City
from models.country import Country

cities_blueprint = Blueprint("cities", __name__)