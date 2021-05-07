from flask import Blueprint, jsonify
from app.models import Ingredient


ingredient_routes = Blueprint('ingredients', __name__)

# get all ingredients route. WORKS
@ingredient_routes.route('/')
def all_ingredients():
  ingredients = Ingredient.query.all()
  return {'ingredients': [ingredient.to_dict() for ingredient in ingredients]}
