from .db import db


class Drink(db.Model):
    __tablename__ = 'drinks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    isAlcoholic = db.Column(db.Boolean)
    photo_url = db.Column(db.String(1000))
    instructions = db.Column(db.String(1500), nullable=False)
    favorites = db.Column(db.Integer, default=0)

    favorite_drink = db.relationship('Favorite_drink', backref='drinks')
    drink_ingredient = db.relationship('Drink_ingredient', backref='drinks')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "isAlcoholic": self.isAlcoholic,
            "photo_url": self.photo_url,
            "instructions": self.instructions,
            "favorites": self.favorites
        }
