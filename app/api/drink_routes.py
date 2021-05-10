from flask import Blueprint, jsonify, request
from app.models import Drink
from app.models import db, Ingredient
from app.awsupload import upload_file_to_s3, allowed_file, get_unique_filename
from flask_login import login_required

drink_routes = Blueprint('drinks', __name__)


# get all drinks route. WORKS
@drink_routes.route('/')
def all_drinks():
  drinks = Drink.query.all()
  return {'drinks': [drink.to_dict() for drink in drinks]}

# convert photo file to url AND uploads to AWS bucket. WORKS
@drink_routes.route('/photo', methods=["POST"])
def photo_file_convert():
  if "photo" not in request.files:
    return {"errors": "photo required"}, 400

  photo = request.files["photo"]

  if not allowed_file(photo.filename):
    return {"errors": "file type not permitted"}, 400

  photo.filename = get_unique_filename(photo.filename)

  upload = upload_file_to_s3(photo)

  if "url" not in upload:
    return upload, 400

  url = upload["url"]
  return {"photo_url": url}

# Create drink route. WORKS
@drink_routes.route('/create', methods=['POST'])
@login_required
def create_drink():
  print(request.json, "---------------------------------")
  newAuthorId = request.json["authorId"]
  newName = request.json["name"]
  newIsAlcoholic = request.json["isAlcoholic"]
  newInstructions = request.json["instructions"]
  newIngredients = request.json["ingredients"]
  newPhoto_url = request.json["photo_url"]

  ingredients = []
  for ingredient in newIngredients:
    ingredients.append(Ingredient.query.get(ingredient))

  newDrink = Drink(authorId = newAuthorId, name = newName, isAlcoholic = newIsAlcoholic, instructions = newInstructions, photo_url = newPhoto_url)

  db.session.add(newDrink)
  db.session.commit()
  for ingredient in ingredients:
    db.session.execute(f"""insert into drink_ingredients ("drinkId", "ingredientId")
    values ({newDrink.id}, {ingredient.id});""")
  db.session.commit()
  return newDrink.to_dict()


  # newAuthorId = 1
  # newName = "test-drink6"
  # newIsAlcoholic = True
  # newInstructions = "please work"
  # newPhoto_url = "www.nothing.com"
  # newIngredients = ["Gin", "Absinthe"]
