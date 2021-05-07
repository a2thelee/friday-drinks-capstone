from flask import Blueprint, jsonify

drink_ingredient_routes = Blueprint('drink_ingredients', __name__)


# get all drink_ingredients. narrow down later to only get 1
@drink_ingredient_routes.route('/')
def all_drink_ingredients():
  drink_ingredients = Drink_ingredient.query.all()
  return {'drinkIngredients': [drink_ingredient.to_dict() for drink_ingredient in drink_ingredients]}
