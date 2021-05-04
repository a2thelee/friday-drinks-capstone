from .db import db
from .drink import Drink
from .user import User


class Favorite_drink(db.Model):
    __tablename__ = 'favorite_drinks'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    drinkId = db.Column(db.Integer, db.ForeignKey('drinks.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "drinkId": self.drinkId
        }
