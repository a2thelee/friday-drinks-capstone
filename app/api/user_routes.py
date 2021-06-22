from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, Favorite_drink, db

user_routes = Blueprint('users', __name__)

@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/favorites', methods = ["POST"])
@login_required
def make_favorite():
    # drinkId = request.json["drinkId"]

    favorite_drink = Favorite_drink(userId=current_user.id, drinkId = request.json["drinkId"])
    db.session.add(favorite_drink)
    db.session.commit()
    return favorite_drink.to_dict() #ask about this later

@user_routes.route('/favorites', methods = ["DELETE"])
@login_required
def un_favorite():
    # drinkId = request.json["drinkId"]

    favorite_drink = Favorite_drink.query.get(request.json["favoriteId"])
    db.session.delete(favorite_drink)
    db.session.commit()
    return jsonify("Success!") #ask about this later
