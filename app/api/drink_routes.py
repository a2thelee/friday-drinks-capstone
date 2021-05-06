from flask import Blueprint, jsonify
from app.models import Drink

drink_routes = Blueprint('drinks', __name__)

@drink_routes.route('/')
def all_drinks():
  drinks = Drink.query.all()
  return {'drinks': [drink.to_dict() for drink in drinks]}
