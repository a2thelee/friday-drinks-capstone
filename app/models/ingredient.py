from .db import db
from .drink_ingredient import Drink_ingredients


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)

    drinks = db.relationship('Drink', secondary=Drink_ingredients)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
