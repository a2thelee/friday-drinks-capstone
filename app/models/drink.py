from .db import db
from .drink_ingredient import Drink_ingredients


class Drink(db.Model):
    __tablename__ = 'drinks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    isAlcoholic = db.Column(db.Boolean)
    photo_url = db.Column(db.String(1000))
    instructions = db.Column(db.String(1500), nullable=False)
    authorId = db.Column(db.Integer)
    favorites = db.Column(db.Integer, default=0)

    favorite_drink = db.relationship('Favorite_drink', backref='drinks')
    ingredients = db.relationship('Ingredient', secondary=Drink_ingredients)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "isAlcoholic": self.isAlcoholic,
            "photo_url": self.photo_url,
            "instructions": self.instructions,
            "authorId": self.authorId,
            "favorites": self.favorites,
            "show": False,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients],
            "number_of_favorites": len(self.favorite_drink)
        }
