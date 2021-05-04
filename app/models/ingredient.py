from .db import db


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)

    drink_ingredient = db.relationship(
        'Drink_ingredient', backref='ingredients')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
