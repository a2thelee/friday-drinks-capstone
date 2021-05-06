from app.models import db, Favorite_drink

def seed_favorite_drinks():
  favoriteDrinks= [
    Favorite_drink(userId=1, drinkId=1)
  ]

  db.session.add_all(favoriteDrinks)

  db.session.commit()

def undo_favorite_drinks():
  db.session.execute('TRUNCATE favorite_drinks RESTART IDENTITY CASCADE')
  db.session.commit()
