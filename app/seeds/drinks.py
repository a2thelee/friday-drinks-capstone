from app.models import db, Drink

def seed_drinks():
  drinks = [
    Drink(name="Old Fashioned", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg", instructions="1-1.5 oz of bourbon, 2 dashes of Angostura bitters, 1 sugar cube, and a dash of water. Place sugar cube in old fashioned glass and saturate with bitters, add a dash of plain water. Muddle until dissolved.\r\nFill the glass with ice cubes and add whiskey.\r\n\r\nGarnish with orange twist, and a cocktail cherry."
    ),
    Drink(name="Mojito", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg", instructions="2-3 oz of light rum, 1 squeeze of lime juice, 2 tsp of sugar, and 2-4oz of soda water. Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw."
    ),
    Drink(name="Martini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/71t8581504353095.jpg", instructions="1 2/3oz, 1/3oz of dry vermouth, 1 olive. Straight: Pour all ingredients into mixing glass with ice cubes. Stir well. Strain in chilled martini cocktail glass. Squeeze oil from lemon peel onto the drink, or garnish with olive."
    ),
    Drink(name="Daiquiri", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/mrz9091589574515.jpg", instructions="1 1/2oz of light rum, juice of 1/2 of 1 lime, 1 tsp of powdered sugar. Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass."
    ),
    Drink(name="Cosmopolitan", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/kpsajh1504368362.jpg", instructions="1 1/4oz Absolut Citron, 1/4oz of lime juice, 1/4oz of cointreau, 1/4 cup of cranberry juice. Pour all ingredients in mixing glass half filled with ice, shake and strain into chilled Martini glass."
    ),
    Drink(name="Caipirinha", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/jgvn7p1582484435.jpg", instructions="2 tsp sugar, 1 lime, 2 1/2oz of cachaca. Place lime and sugar into old fashioned glass and muddle (mash the two ingredients together using a muddler or a wooden spoon). Fill the glass with ice and add the Cachaça."
    ),
     Drink(name="White Russian", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vsrupw1472405732.jpg", instructions="2oz of coffee liqueur, 1 oz of light cream. Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve."
    ),
     Drink(name="Pina Colada", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/cpf4j51504371346.jpg", instructions="3oz light rum, 3 tblspn of coconut milk, 3tbl spoon of pineapple. Mix with crushed ice in blender until smooth. Pour into chilled glass, garnish and serve"
    ),
     Drink(name="Negroni", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/qgdu971561574065.jpg", instructions="1oz gin, 1oz campari, 1oz sweet vermouth. Stir into glass over ice, garnish and serve."
    ),
     Drink(name="Bramble", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/lvzl3r1504372526.jpg", instructions="1.5 oz of gin, 1/2oz of lemon juice, 1/2 oz of sugar syrup, 1.5 of creme de mure. Fill glass with crushed ice. Build gin, lemon juice and simple syrup over. Stir, and then pour blackberry liqueur over in a circular fashion to create marbling effect. Garnish with two blackberries and lemon slice."
    ),
    Drink(name="Margarita", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg", instructions="1 1/2oz tequila, 1/2oz triple sec, 1oz of lime juice, salt. Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass."
    ),
    Drink(name="Dark and Stormy", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t1tn0s1504374905.jpg", instructions="1.5oz of dark rum, 3oz ginger beer. In a highball glass filled with ice add 6cl dark rum and top with ginger beer. Garnish with lime wedge."
    ),
    Drink(name="Cuba Libre", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/wmkbfj1606853905.jpg", instructions="1-2 shots of dark rum, a squeeze of lime, and coca-cola and ice. Build all ingredients in a Collins glass filled with ice. Garnish with lime wedge."
    ),
    Drink(name="Sazerac", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vvpxwy1439907208.jpg", instructions="1 tsp of Ricard, 1/2 tsp of superfine sugar, 2 dashes of peychaud bitters, 1 tsp of water, 2oz of bourbon, 1 twist of lemon peel. Rinse a chilled old-fashioned glass with the absinthe, add crushed ice, and set it aside. Stir the remaining ingredients over ice and set it aside. Discard the ice and any excess absinthe from the prepared glass, and strain the drink into the glass. Add the lemon peel for garnish."
    ),
    Drink(name="Bloody Mary", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t6caa21582485702.jpg", instructions="1 1/2oz vodka, 3oz tomato juice, 1 dash of lemon juice, 1/2 tsp worcestershire sauce, 2-3 drops of tabasco sauce, and 1 wedge of lime. Stirring gently, pour all ingredients into highball glass. Garnish."
    ),
    Drink(name="Manhattan", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/yk70e31606771240.jpg", instructions="3/4 sweet vermouth, 2 1/2oz blended bourbon, a dash of angostura bitters, 2-3 ice cubes, 1 maraschino cherry, 1 twist orange peel. Stirred over ice, strained into a chilled glass, garnished, and served up."
    ),
    Drink(name="Long Island Iced Tea", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/wx7hsg1504370510.jpg", instructions="1/2oz vodka, 1/2oz tequila, 1/2oz light rum, 1/2oz gin, coca-cola, a twist of lemon peel. Mix all contents in a highball glass and sitr gently. Add dash of Coca-Cola for the coloring and garnish with lemon or lime twist."
    ),
    Drink(name="Mai Tai", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/twyrrp1439907470.jpg", instructions="1oz light rum, 1/2oz orgeat syrup, 1/2oz triple sec, 1 1/2oz sweet and sour, 1 cherry. Shake all ingredients with ice. Strain into glass. Garnish and serve with straw."
    ),
    Drink(name="Amaretto Sour", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/xnzc541493070211.jpg", instructions="1 1/2oz amaretto, 3oz sour mix. Shake and strain. Garnish with a cherry and an orange slice."
    ),
    Drink(name="Singapore Sling", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/7dozeg1582578095.jpg", instructions="1/2oz cherry brandy, 1/2oz grenadine, 1oz gin, 2oz sweet and sour, carbonated water, cherry. Pour all ingredients into cocktail shaker filled with ice cubes. Shake well. Strain into highball glass. Garnish with pineapple and cocktail cherry."
    ),
    Drink(name="French Martini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/clth721504373134.jpg", instructions="1.5oz vodka, 1/2oz raspberry liqueur, 1/2oz pineapple juice. Pour all ingredients into shaker with ice cubes. Shake well and strain into a chilled cocktail glass. Squeeze oil from lemon peel onto the drink."
    ),
    Drink(name="Espresso Martini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/n0sx531504372951.jpg", instructions="1.5oz vodka, 1/2oz kahlua, dash of sugar syrup. Pour ingredients into shaker filled with ice, shake vigorously, and strain into chilled martini glass"
    ),
    Drink(name="Strawberry Daiquiri", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/deu59m1504736135.jpg", instructions="1/2oz strawberry schnapps, 1oz light rum, 1oz lime juice, 1tsp powdered sugar, 1oz strawberries. Pour all ingredients into shaker with ice cubes. Shake well. Strain in chilled cocktail glass."
    ),
    Drink(name="Moscow Mule", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/3pylqc1504370988.jpg", instructions="2oz vodka, 2oz lime juice, 8oz ginger beer. Combine vodka and ginger beer in a highball glass filled with ice. Add lime juice. Stir gently. Garnish."
    ),
    Drink(name="Clover Club", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t0aja61504348715.jpg", instructions="1 1/2oz gin, 2 tsp Grenadine, juice of 1/2 a lemon, 1 egg white. Dry shake ingredients to emulsify, add ice, shake and served straight up."
    ),
    Drink(name="Mint Julep", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/squyyq1439907312.jpg", instructions="4 fresh mint leaves, 1 1/2oz bourbon, 1tsp powdered sugar, 2 tsp water. In a highball glass gently muddle the mint, sugar and water. Fill the glass with cracked ice, add Bourbon and stir well until the glass is well frosted. Garnish with a mint sprig."
    ),
    Drink(name="John Collins", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/0t4bv71606854479.jpg", instructions="2oz bourbon, 1oz lemon juice, 1 tsp of superfine sugar, 3oz of club soda, 1 maraschino cherry, 1 orange. Pour all ingredients directly into highball glass filled with ice. Stir gently. Garnish. Add a dash of Angostura bitters."
    ),
    Drink(name="Gin Sour", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/noxp7e1606769224.jpg", instructions="2oz gin, 1oz lemon juice, 1/2 tsp of superfine sugar, 1 orange, 1 maraschino cherry. In a shaker half-filled with ice cubes, combine the gin, lemon juice, and sugar. Shake well. Strain into a sour glass and garnish with the orange slice and the cherry."
    ),
    Drink(name="White Lady", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/jofsaz1504352991.jpg", instructions="1.5oz gin, 1oz triple sec, 1/2oz lemon juice. Add all ingredients into cocktail shaker filled with ice. Shake well and strain into large cocktail glass."
    ),
    Drink(name="Black Russian", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/8oxlqf1606772765.jpg", instructions="3/4oz coffee liqueur, 1 1/2oz vodka. Pour the ingredients into an old fashioned glass filled with ice cubes. Stir gently."
    ),
    Drink(name="Funk and Soul", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/qtv83q1596015790.jpg", instructions="2 shots rum, 1 shot apricot nectar, 1 shot pomegranate juice, juice of 1/2 lemon, top with soda water. Mix all ingredients together and strain into a Collins glass. Use Jamaican rum where possible for a more authentic taste."
    ),
    Drink(name="Brandy Alexander", isAlcoholic=True, photo_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Brandy_Alexander_on_the_Rocks.jpg", instructions="1oz brandy, 1 oz creme de cacao, 1 oz light cream, nutmeg. Shake all ingredients (except nutmeg) with ice and strain contents into a cocktail glass. Sprinkle nutmeg on top and serve."
    ),
    Drink(name="French 75", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/hrxfbl1606773109.jpg", instructions="1 1/2oz gin, 2 tsp superfine sugar, 1 1/2 oz lemon juice, 4oz chilled champagne, 1 orange, 1 maraschino cherry. Combine gin, sugar, and lemon juice in a cocktail shaker filled with ice. Shake vigorously and strain into a chilled champagne glass. Top up with Champagne. Stir gently."
    ),
    Drink(name="Autumn Garibaldi", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/ne7re71604179012.jpg", instructions="1 1/2oz campari, 2 1/2oz orange juice, 2 1/2oz ginger beer, orange peel. Pour all ingredients into a glass over ice and stir with a bar spoon. Garnish with some orange slices."
    ),
    Drink(name="Gin Fizz", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/drtihp1606768397.jpg", instructions="2oz gin, juice of 1/2 lemon, 1tsp powdered sugar, carbonated water. Shake all ingredients with ice cubes, except soda water. Pour into glass. Top with soda water."
    ),
    Drink(name="Rusty Nail", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/yqsvtw1478252982.jpg", instructions="1 1/2oz scotch, 1/2oz drambuie, 1 twist of lemon peel. Pour the Scotch and Drambuie into an old-fashioned glass almost filled with ice cubes. Stir well. Garnish with the lemon twist."
    ),
    Drink(name="Pisco Sour", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/tsssur1439907622.jpg", instructions="2oz pisco, 1oz lemon juice, 1-2 tblsp sugar, 1 egg white, ice. Vigorously shake and strain contents in a cocktail shaker with ice cubes, then pour into glass and garnish with bitters.\r\n"
    ),
    Drink(name="Rum Runner", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/vqws6t1504888857.jpg", instructions="1 1/2oz malibu rum, 1oz blackberry brandy, 3-4oz orange juice, 3-4oz pineapple juice, 3-4oz cranberry juice. Mix all ingredients in glass & add ice."
    ),
    Drink(name="Wine Punch", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/txustu1473344310.jpg", instructions="1 bottle red wine, 2 lemons, 1 cup of orange juice, 1 cup pineapple juice. Combine all of the ingredients and pour over a block of ice."
    ),
    Drink(name="Sangria", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/xrvxpp1441249280.jpg", instructions="1 bottle red wine, 1/2 cup sugar, 1 cup orange juice, 1 cup lemon juice, cloves, cinnamon. Mix all together in a pitcher and refrigerate. Add cloves and cinnamon sticks to taste. Serve in wine glasses."
    ),
    Drink(name="Kir Royale", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/yt9i7n1504370388.jpg", instructions="1 part creme de cassis, 5 parts champagne. Pour Creme de cassis in glass, gently pour champagne on top"
    ),
    Drink(name="Bellini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/eaag491504367543.jpg", instructions="6oz champagne, 1oz peach schnapps. Pour peach purée into chilled flute, add sparkling wine. Stir gently."
    ),
    Drink(name="Lemon Drop", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/mtpxgk1504373297.jpg", instructions="1 1/2 shot absolut vodka, 1 1/2 shot cointreau, juice of one wedge of lemon. Shake and strain into a chilled cocktail glass rimmed with sugar."
    ),
    Drink(name="Pink Gin", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/qyr51e1504888618.jpg", instructions="3 dashes of angostura bitters, 2oz gin. Pour the bitters into a wine glass. Swirl the glass to coat the inside with the bitters, shake out the excess, add ice. Pour the gin into the glass. Garnish with straberries or lemon wedge"
    ),
    Drink(name="Salty Dog", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/4vfge01504890216.jpg", instructions="5oz grapefruit juice, 1 1/2oz gin, 1/4tsp salt. Pour all ingredients over ice cubes in a highball glass. Stir well and serve. (Vodka may be substituted for gin, if preferred.)"
    ),
    Drink(name="B-52", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/5a3vg61504372070.jpg", instructions="1/3oz bailey's irish cream, 1/3oz grand marnier, 1/4oz kahlua. Layer ingredients into a shot glass. Serve with a stirrer."
    ),
    Drink(name="Irish Spring", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/sot8v41504884783.jpg", instructions="1oz irish whiskey, 1/2oz peach brandy, 1oz orange juice, 1oz sweet and sour, 1 slice of orange, 1 maraschino cherry. Pour all ingredients (except orange slice and cherry) into a collins glass over ice cubes. Garnish with the slice of orange, add the cherry on top, and serve."
    ),
    Drink(name="Screwdriver", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/8xnyke1504352207.jpg", instructions="2oz vodka, 4oz orance juice. Mix in a highball glass with ice. Garnish and serve."
    ),
    Drink(name="French Connection", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/zaqa381504368758.jpg", instructions="1 1/2oz cognac, 3/4oz amaretto. our all ingredients directly into old fashioned glass filled with ice cubes. Stir gently."
    ),
    Drink(name="Paloma", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/samm5j1513706393.jpg", instructions="3oz grapefruit juice, 1 1/2oz tequila, 1/2oz sugar syrup, 1/4oz lime juice. Stir together and serve over ice, garnish with a grapefruit slice."
    ),

    Drink(name="Royal Fizz", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/wrh44j1504390609.jpg", instructions="1oz gin, 2oz sweet and sour, egg white, coca cola. Shake all ingredients (except cola) with ice and strain into a chilled collins glass. Fill with cola and serve."
    ),
    Drink(name="Strawberry Margarita", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/tqyrpw1439905311.jpg", instructions="1/2oz strawberry schnapps, 1oz tequila, 1/2oz triple sec, 1oz lemon juice, 1oz strawberries. Rub rim of cocktail glass with lemon juice and dip rim in salt. Shake schnapps, tequila, triple sec, lemon juice, and strawberries with ice, strain into the salt-rimmed glass, and serve."
    ),
    Drink(name="Sea breeze", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/7rfuks1504371562.jpg", instructions="1 1/2oz vodka, 4oz cranberry juice, 1oz grapefruit juice. Build all ingredients in a highball glass filled with ice. Garnish with lime wedge."
    ),
    Drink(name="Royal Gin Fizz", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/pe1x1c1504735672.jpg", instructions="2oz gin, juice of 1/2 lemon, 1tsp powdered sugar, egg white, carbonated water. Shake all ingredients (except carbonated water) with ice and strain into a highball glass over two ice cubes. Fill with carbonated water, stir, and serve.",
    ),
    Drink(name="Gin Basil Smash", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/jqh2141572807327.jpg", instructions="2oz gin, 1/2oz lemon juice, 1/2oz sugar syrup, basil. Muddle Basil leaves (~ 10) with Suggar Syrup in a shaker. Add Gin an Lemon Juice.\r\nFilter and serve in a tumbler with ice",
    ),
    Drink(name="Abbey Martini", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/2mcozt1504817403.jpg", instructions="2 shots gin, 1 shot sweet vermouth, 1 shot orange juice, 3 dashes angostura bitters. Put all ingredients into a shaker and mix, then strain contents into a chilled cocktail glass."
    ),
    Drink(name="Bacardi Cocktail", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/n433t21504348259.jpg", instructions="1 3/4oz bacardi, 1oz lime juice, 1/2tsp sugar syrup, 1 dash of grenadine. Shake together with ice. Strain into glass and serve.",
    ),
    Drink(name="Golden dream", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/qrot6j1504369425.jpg", instructions="2 parts galliano, 2 parts triple sec, 2 parts orange juice, 1 part cream. Shake with cracked ice. Strain into glass and serve."
    ),
    Drink(name="Sex on the Beach", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/lijtw51551455287.jpg", instructions="1oz vodka, 3/4oz peach schnapps, cranberry juice, grapefruit juice. Build all ingredients in a highball glass filled with ice. Garnish with orange slice.",
    ),
    Drink(name="Tequila Sunrise", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg", instructions="1 1/2oz tequila, 3/4 cup orange juice, 3/4oz grenadine, orange slice, maraschino cherry. Pour the tequila and orange juice into glass over ice. Add the grenadine, which will sink to the bottom. Stir gently to create the sunrise effect. Garnish and serve.",
    ),

    Drink(name="Brooklyn", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/ojsezf1582477277.jpg", instructions="2 oz rye whiskey, 1 oz dry vermouth, 1/4 oz maraschino liqueur, 3 dashes angostura bitters, 1 maraschino cherry. Combine ingredients with ice and stir until well-chilled. Strain into a chilled cocktail glass.",
    ),
    Drink(name="Caribbean Boilermaker", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/svsxsv1454511666.jpg", instructions="1 bottle of corona, 1 shot of light rum. Pour the Corona into an 18oz beer glass pour the rum into the beer."
    ),
    Drink(name="Gimlet", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/3xgldt1513707271.jpg", instructions="2 1/2 oz gin, 1/2 oz lime juice, 1/2 oz sugar syrup, 1 lime. Add all the ingredients to a shaker and fill with ice. Shake, and strain into a chilled cocktail glass or an Old Fashioned glass filled with fresh ice. Garnish with a lime wedge."
    ),
    Drink(name="Porto flip", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/64x5j41504351518.jpg", instructions="3 parts brandy, 9 parts port, 2 parts egg yolk. Shake ingredients together in a mixer with ice. Strain into glass, garnish and serve."
    ),
    Drink(name="Raspberry Cooler", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/suqyyx1441254346.jpg", instructions="2 oz raspberry vodka, 4 oz lemon lime soda, ice. Pour the raspberry vodka and soda into a highball glass almost filled with ice cubes. Stir well."
    ),
    Drink(name="Sidecar", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/x72sik1606854964.jpg", instructions="2 oz cognac, 1/2 oz cointreau, 1 oz lemon juice. Pour all ingredients into cocktail shaker filled with ice. Shake well and strain into cocktail glass."
    ),
    Drink(name="Champagne Cocktail", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/t5pv461606773026.jpg", instructions="chilled champagne, 1 sugar cube, 2 dashes of angostura bitters, 1 twist of lemon peel, dash of cognac. Add dash of Angostura bitter onto sugar cube and drop it into champagne flute. Add cognac followed by gently pouring chilled champagne. Garnish with orange slice and maraschino cherry."
    ),
    Drink(name="Godfather", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/e5zgao1582582378.jpg", instructions="1 1/2 oz scotch, 3/4 oz amaretto. Pour all ingredients directly into old fashioned glass filled with ice cubes. Stir gently."
    ),
    Drink(name="Hemingway Special", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/jfcvps1504369888.jpg", instructions="12 parts rum, 8 parts grapefruit juice, 3 parts maraschino liqueur, 3 parts lime juice. Pour all ingredients into a shaker with ice. Shake."
    ),
    Drink(name="Frozen Pineapple Daiquiri", isAlcoholic=True, photo_url="https://www.thecocktaildb.com/images/media/drink/k3aecd1582481679.jpg", instructions="1 1/2 oz light rum, 4 chunks pineapple, 1 tblsp lime juice, 1/2 tsp sugar. Combine all ingredients with 1 cup of crushed ice in an electric blender. Blend at a low speed for a short length of time. Pour into a cocktail glass and serve."
    ),
  ]

  # Drink(name= isAlcoholic=True, photo_url= instructions=
  #   ),

  db.session.add_all(drinks)

  db.session.commit()

def undo_drinks():
  db.session.execute('TRUNCATE drinks RESTART IDENTITY CASCADE')
  db.session.commit()
