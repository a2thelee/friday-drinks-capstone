from flask import Blueprint, jsonify
from app.models import Favorite_drink


favorite_drink_routes = Blueprint('favorite_drinks', __name__)

# get all favorite drinks route. WORKS
@favorite_drink_routes.route('/')
def all_favorites():
  favorites = Favorite_drink.query.all()
  return {'favorites': [favorite.to_dict() for favorite in favorites]}
