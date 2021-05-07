from flask import Blueprint, jsonify
from app.models import Drink
from app.models import Ingredient

drink_routes = Blueprint('drinks', __name__)


# get all drinks route. WORKS
@drink_routes.route('/')
def all_drinks():
  drinks = Drink.query.all()
  return {'drinks': [drink.to_dict() for drink in drinks]}

# create a drink route. TESTING
# @drink_routes.route('/create', methods=["POST"])
# def create_Drink():
