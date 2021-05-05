from app.models import db, Drink

def seed_drinks():
  drinks = [
    Drink(name="Old Fashioned", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg", instructions="Place sugar cube in old fashioned glass and saturate with bitters, add a dash of plain water. Muddle until dissolved.\r\nFill the glass with ice cubes and add whiskey.\r\n\r\nGarnish with orange twist, and a cocktail cherry."
    ),
    Drink(name="Mojito", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg", instructions="Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw."
    ),
    Drink(name="Martini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/71t8581504353095.jpg", instructions="Straight: Pour all ingredients into mixing glass with ice cubes. Stir well. Strain in chilled martini cocktail glass. Squeeze oil from lemon peel onto the drink, or garnish with olive."
    ),
    Drink(name="Daiquiri", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/mrz9091589574515.jpg", instructions="Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass."
    ),
    Drink(name="Cosmopolitan", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/kpsajh1504368362.jpg", instructions="Pour all ingredients in mixing glass half filled with ice, shake and strain into chilled Martini glass."
    ),
    Drink(name="Caipirinha", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/jgvn7p1582484435.jpg", instructions="Place lime and sugar into old fashioned glass and muddle (mash the two ingredients together using a muddler or a wooden spoon). Fill the glass with ice and add the Cachaça."
    ),
     Drink(name="White Russian", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vsrupw1472405732.jpg", instructions="Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve."
    ),
     Drink(name="Pina Colada", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/cpf4j51504371346.jpg", instructions="Mix with crushed ice in blender until smooth. Pour into chilled glass, garnish and serve"
    ),
     Drink(name="Negroni", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/qgdu971561574065.jpg", instructions="Stir into glass over ice, garnish and serve."
    ),
     Drink(name="Bramble", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/lvzl3r1504372526.jpg", instructions="Fill glass with crushed ice. Build gin, lemon juice and simple syrup over. Stir, and then pour blackberry liqueur over in a circular fashion to create marbling effect. Garnish with two blackberries and lemon slice."
    ),
    Drink(name="Margarita", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg", instructions="Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass."
    ),
    Drink(name="Dark and Stormy", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t1tn0s1504374905.jpg", instructions="In a highball glass filled with ice add 6cl dark rum and top with ginger beer. Garnish with lime wedge."
    ),
    Drink(name="Cuba Libre", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/wmkbfj1606853905.jpg", instructions="Build all ingredients in a Collins glass filled with ice. Garnish with lime wedge."
    ),
    Drink(name="Sazerac", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vvpxwy1439907208.jpg", instructions="Rinse a chilled old-fashioned glass with the absinthe, add crushed ice, and set it aside. Stir the remaining ingredients over ice and set it aside. Discard the ice and any excess absinthe from the prepared glass, and strain the drink into the glass. Add the lemon peel for garnish."
    ),
    Drink(name="Bloody Mary", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t6caa21582485702.jpg", instructions="Stirring gently, pour all ingredients into highball glass. Garnish."
    ),
    Drink(name="Manhattan", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/yk70e31606771240.jpg", instructions="Stirred over ice, strained into a chilled glass, garnished, and served up."
    ),
    Drink(name="Long Island Iced Tea", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/wx7hsg1504370510.jpg", instructions="Mix all contents in a highball glass and sitr gently. Add dash of Coca-Cola for the coloring and garnish with lemon or lime twist."
    ),
    Drink(name="Mai Tai", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/twyrrp1439907470.jpg", instructions="Shake all ingredients with ice. Strain into glass. Garnish and serve with straw."
    ),
    Drink(name="Amaretto Sour", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/xnzc541493070211.jpg", instructions="Shake and strain. Garnish with a cherry and an orange slice."
    ),
    Drink(name="Singapore Sling", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/7dozeg1582578095.jpg", instructions="Pour all ingredients into cocktail shaker filled with ice cubes. Shake well. Strain into highball glass. Garnish with pineapple and cocktail cherry."
    ),
  ]

  # Drink(name="", isAlcoholic=True, photo_url="", instructions=""
  #   ),

  db.session.add_all(drinks)

  db.session.commit()

def undo_drinks():
  db.session.execute('TRUNCATE drinks RESTART IDENTITY CASCADE')
  db.session.commit()
