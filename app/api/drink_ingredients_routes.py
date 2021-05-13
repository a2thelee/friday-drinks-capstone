from flask import Blueprint, jsonify

drink_ingredient_routes = Blueprint('drink_ingredients', __name__)


# get all drink_ingredients. works
@drink_ingredient_routes.route('/')
def all_drink_ingredients():
  drink_ingredients = Drink_ingredient.query.all()
  return {'drinkIngredients': [drink_ingredient.to_dict() for drink_ingredient in drink_ingredients]}

# get one drink_ingredient
# @drink_ingredient_routes.route('/<:id>')
# def get_one_drink_ingredients():
#   one_drink_ingredients
