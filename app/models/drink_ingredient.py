from .db import db
from .drink import Drink
from .ingredient import Ingredient


class Drink_ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drinkId = db.Column(db.Integer, db.ForeignKey('drinks.id'), nullable=False)
    ingredientId = db.Column(db.Integer, db.ForeignKey(
        'ingredients.id'), nullable=False)

    def to_dict(self):
        return{
            "id": self.id,
            "drinkId": self.drinkId,
            "ingredientId": self.ingredientId
        }
