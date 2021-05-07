from .db import db
# from .drink import Drink
# from .ingredient import Ingredient


# class Drink_ingredient(db.Model):
#     __tablename__ = 'drink_ingredients'

#     id = db.Column(db.Integer, primary_key=True)
#     drinkId = db.Column(db.Integer, db.ForeignKey('drinks.id'), nullable=False)
#     ingredientId = db.Column(db.Integer, db.ForeignKey(
#         'ingredients.id'), nullable=False)

#     def to_dict(self):
#         return{
#             "id": self.id,
#             "drinkId": self.drinkId,
#             "ingredientId": self.ingredientId
#         }

Drink_ingredients = db.Table(
    'drink_ingredients',
    db.Column(
        "drinkId",
        db.Integer,
        db.ForeignKey('drinks.id'),
        primary_key=True
    ),
    db.Column(
        "ingredientId",
        db.Integer,
        db.ForeignKey('ingredients.id'),
        primary_key=True
    )
)
