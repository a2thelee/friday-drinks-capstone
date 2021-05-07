from .db import db


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
