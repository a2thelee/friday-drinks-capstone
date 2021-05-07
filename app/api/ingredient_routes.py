from flask import Blueprint, jsonify
from app.models import Ingredient


ingredient_routes = Blueprint('ingredients', __name__)

# get all ingredients route.
