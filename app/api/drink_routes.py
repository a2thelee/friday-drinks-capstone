from flask import Blueprint, jsonify
from app.models import Drink
from app.models import db, Ingredient

drink_routes = Blueprint('drinks', __name__)


# get all drinks route. WORKS
@drink_routes.route('/')
def all_drinks():
  drinks = Drink.query.all()
  return {'drinks': [drink.to_dict() for drink in drinks]}

# create a drink route. TESTING
# @drink_routes.route('/create', methods=["POST"])
# def create_Drink():
@drink_routes.route('/test')
def test_drink():
  test = Ingredient.query.filter(Ingredient.name == "Gin").one()
  # test = Ingredient.query.get(1)
  return test.to_dict()

@drink_routes.route('/create')
#@login required
def create_drink():
  # newAuthorId = request.json["authorId"]
  # newName = request.json["name"]
  # newIsAlcoholic = request.json["isAlcoholic"]
  # newInstructions = request.json["instructions"]
  # newPhoto_url = request.json["phoro_url"]
  # newIngredients = request.json["ingredients"]
  newAuthorId = 1
  newName = "test-drink6"
  newIsAlcoholic = True
  newInstructions = "please work"
  newPhoto_url = "www.nothing.com"
  newIngredients = ["Gin", "Absinthe"]

  ingredients = []
  for ingredient in newIngredients:
    ingredients.append(Ingredient.query.filter(Ingredient.name==ingredient).one())

  newDrink = Drink(authorId = newAuthorId, name = newName, isAlcoholic = newIsAlcoholic, instructions = newInstructions, photo_url = newPhoto_url)

  db.session.add(newDrink)
  db.session.commit()
  for ingredient in ingredients:
    db.session.execute(f"""insert into drink_ingredients ("drinkId", "ingredientId")
    values ({newDrink.id}, {ingredient.id});""")
  db.session.commit()
  return newDrink.to_dict()
