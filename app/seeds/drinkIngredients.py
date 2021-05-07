from app.models import db, Drink, Ingredient

def seed_drink_ingredients():
  drink1=Drink.query.get(1)
  drink1.ingredients.append(Ingredient.query.get(72))

  drink1.ingredients.append(Ingredient.query.get(20))

  drink1.ingredients.append(Ingredient.query.get(429))

  drink1.ingredients.append(Ingredient.query.get(462))

  drink2=Drink.query.get(2)
  drink2.ingredients.append(Ingredient.query.get(271))

  drink2.ingredients.append(Ingredient.query.get(274))

  drink2.ingredients.append(Ingredient.query.get(429))

  drink2.ingredients.append(Ingredient.query.get(304))

  drink2.ingredients.append(Ingredient.query.get(411))

  drink3=Drink.query.get(3)
  drink3.ingredients.append(Ingredient.query.get(203))

  drink3.ingredients.append(Ingredient.query.get(171))

  drink3.ingredients.append(Ingredient.query.get(309))

  drink4=Drink.query.get(4)
  drink4.ingredients.append(Ingredient.query.get(271))

  drink4.ingredients.append(Ingredient.query.get(274))

  drink4.ingredients.append(Ingredient.query.get(365))

  drink5=Drink.query.get(5)
  drink5.ingredients.append(Ingredient.query.get(7))

  drink5.ingredients.append(Ingredient.query.get(275))

  drink5.ingredients.append(Ingredient.query.get(129))

  drink5.ingredients.append(Ingredient.query.get(138))

  drink6=Drink.query.get(6)
  drink6.ingredients.append(Ingredient.query.get(429))

  drink6.ingredients.append(Ingredient.query.get(274))

  drink6.ingredients.append(Ingredient.query.get(77))

  drink7=Drink.query.get(7)
  drink7.ingredients.append(Ingredient.query.get(461))
  drink7.ingredients.append(Ingredient.query.get(127))

  drink7.ingredients.append(Ingredient.query.get(270))

  drink8=Drink.query.get(8)
  drink8.ingredients.append(Ingredient.query.get(271))

  drink8.ingredients.append(Ingredient.query.get(122))

  drink8.ingredients.append(Ingredient.query.get(352))

  drink9=Drink.query.get(9)
  drink9.ingredients.append(Ingredient.query.get(203))

  drink9.ingredients.append(Ingredient.query.get(79))

  drink9.ingredients.append(Ingredient.query.get(435))

  drink10=Drink.query.get(10)
  drink10.ingredients.append(Ingredient.query.get(203))

  drink10.ingredients.append(Ingredient.query.get(263))

  drink10.ingredients.append(Ingredient.query.get(430))

  drink10.ingredients.append(Ingredient.query.get(151))

  drink11=Drink.query.get(11)
  drink11.ingredients.append(Ingredient.query.get(442))

  drink11.ingredients.append(Ingredient.query.get(449))

  drink11.ingredients.append(Ingredient.query.get(275))

  drink11.ingredients.append(Ingredient.query.get(398))

  drink12=Drink.query.get(12)
  drink12.ingredients.append(Ingredient.query.get(163))

  drink12.ingredients.append(Ingredient.query.get(206))

  drink13=Drink.query.get(13)
  drink13.ingredients.append(Ingredient.query.get(163))

  drink13.ingredients.append(Ingredient.query.get(274))

  drink13.ingredients.append(Ingredient.query.get(116))

  drink13.ingredients.append(Ingredient.query.get(241))

  drink14=Drink.query.get(14)
  drink14.ingredients.append(Ingredient.query.get(383))

  drink14.ingredients.append(Ingredient.query.get(429))

  drink14.ingredients.append(Ingredient.query.get(349))

  drink14.ingredients.append(Ingredient.query.get(462))

  drink14.ingredients.append(Ingredient.query.get(72))

  drink14.ingredients.append(Ingredient.query.get(264))

  drink15=Drink.query.get(15)
  drink15.ingredients.append(Ingredient.query.get(461))

  drink15.ingredients.append(Ingredient.query.get(447))

  drink15.ingredients.append(Ingredient.query.get(263))

  drink15.ingredients.append(Ingredient.query.get(480))

  drink15.ingredients.append(Ingredient.query.get(437))

  drink15.ingredients.append(Ingredient.query.get(274))

  drink16=Drink.query.get(16)
  drink16.ingredients.append(Ingredient.query.get(435))

  drink16.ingredients.append(Ingredient.query.get(72))

  drink16.ingredients.append(Ingredient.query.get(20))

  drink16.ingredients.append(Ingredient.query.get(241))

  drink16.ingredients.append(Ingredient.query.get(287))

  drink16.ingredients.append(Ingredient.query.get(317))

  drink17=Drink.query.get(17)
  drink17.ingredients.append(Ingredient.query.get(461))

  drink17.ingredients.append(Ingredient.query.get(442))

  drink17.ingredients.append(Ingredient.query.get(271))

  drink17.ingredients.append(Ingredient.query.get(203))

  drink17.ingredients.append(Ingredient.query.get(116))

  drink17.ingredients.append(Ingredient.query.get(264))

  drink18=Drink.query.get(18)
  drink18.ingredients.append(Ingredient.query.get(271))

  drink18.ingredients.append(Ingredient.query.get(325))

  drink18.ingredients.append(Ingredient.query.get(449))

  drink18.ingredients.append(Ingredient.query.get(436))

  drink18.ingredients.append(Ingredient.query.get(95))

  drink19=Drink.query.get(19)
  drink19.ingredients.append(Ingredient.query.get(17))

  drink19.ingredients.append(Ingredient.query.get(413))

  drink20=Drink.query.get(20)
  drink20.ingredients.append(Ingredient.query.get(36))

  drink20.ingredients.append(Ingredient.query.get(224))

  drink20.ingredients.append(Ingredient.query.get(203))

  drink20.ingredients.append(Ingredient.query.get(436))

  drink20.ingredients.append(Ingredient.query.get(86))

  drink20.ingredients.append(Ingredient.query.get(95))

  drink21=Drink.query.get(21)
  drink21.ingredients.append(Ingredient.query.get(461))

  drink21.ingredients.append(Ingredient.query.get(372))

  drink21.ingredients.append(Ingredient.query.get(352))

  drink22=Drink.query.get(22)
  drink22.ingredients.append(Ingredient.query.get(461))

  drink22.ingredients.append(Ingredient.query.get(254))

  drink22.ingredients.append(Ingredient.query.get(430))

  drink23=Drink.query.get(23)
  drink23.ingredients.append(Ingredient.query.get(425))

  drink23.ingredients.append(Ingredient.query.get(271))

  drink23.ingredients.append(Ingredient.query.get(275))

  drink23.ingredients.append(Ingredient.query.get(365))

  drink23.ingredients.append(Ingredient.query.get(424))

  drink24=Drink.query.get(24)
  drink24.ingredients.append(Ingredient.query.get(461))

  drink24.ingredients.append(Ingredient.query.get(275))

  drink24.ingredients.append(Ingredient.query.get(206))

  drink25=Drink.query.get(25)
  drink25.ingredients.append(Ingredient.query.get(203))

  drink25.ingredients.append(Ingredient.query.get(224))

  drink25.ingredients.append(Ingredient.query.get(263))

  drink25.ingredients.append(Ingredient.query.get(175))

  drink26=Drink.query.get(26)
  drink26.ingredients.append(Ingredient.query.get(304))

  drink26.ingredients.append(Ingredient.query.get(72))

  drink26.ingredients.append(Ingredient.query.get(365))

  drink26.ingredients.append(Ingredient.query.get(462))

  drink27=Drink.query.get(27)
  drink27.ingredients.append(Ingredient.query.get(72))

  drink27.ingredients.append(Ingredient.query.get(263))

  drink27.ingredients.append(Ingredient.query.get(429))

  drink27.ingredients.append(Ingredient.query.get(115))

  drink27.ingredients.append(Ingredient.query.get(287))

  drink27.ingredients.append(Ingredient.query.get(318))

  drink28=Drink.query.get(28)
  drink28.ingredients.append(Ingredient.query.get(203))

  drink28.ingredients.append(Ingredient.query.get(263))

  drink28.ingredients.append(Ingredient.query.get(429))

  drink28.ingredients.append(Ingredient.query.get(318))

  drink28.ingredients.append(Ingredient.query.get(287))

  drink29=Drink.query.get(29)
  drink29.ingredients.append(Ingredient.query.get(203))

  drink29.ingredients.append(Ingredient.query.get(449))

  drink29.ingredients.append(Ingredient.query.get(263))

  drink30=Drink.query.get(30)
  drink30.ingredients.append(Ingredient.query.get(127))

  drink30.ingredients.append(Ingredient.query.get(461))

  drink31=Drink.query.get(31)
  drink31.ingredients.append(Ingredient.query.get(394))

  drink31.ingredients.append(Ingredient.query.get(34))

  drink31.ingredients.append(Ingredient.query.get(363))

  drink31.ingredients.append(Ingredient.query.get(263))

  drink31.ingredients.append(Ingredient.query.get(411))

  drink32=Drink.query.get(32)
  drink32.ingredients.append(Ingredient.query.get(73))

  drink32.ingredients.append(Ingredient.query.get(147))

  drink32.ingredients.append(Ingredient.query.get(270))

  drink32.ingredients.append(Ingredient.query.get(308))

  drink33=Drink.query.get(33)
  drink33.ingredients.append(Ingredient.query.get(203))

  drink33.ingredients.append(Ingredient.query.get(429))

  drink33.ingredients.append(Ingredient.query.get(263))

  drink33.ingredients.append(Ingredient.query.get(92))

  drink33.ingredients.append(Ingredient.query.get(313))

  drink33.ingredients.append(Ingredient.query.get(287))

  drink34=Drink.query.get(34)
  drink34.ingredients.append(Ingredient.query.get(79))

  drink34.ingredients.append(Ingredient.query.get(316))

  drink34.ingredients.append(Ingredient.query.get(206))

  drink34.ingredients.append(Ingredient.query.get(317))

  drink35=Drink.query.get(35)
  drink35.ingredients.append(Ingredient.query.get(203))

  drink35.ingredients.append(Ingredient.query.get(263))

  drink35.ingredients.append(Ingredient.query.get(365))

  drink35.ingredients.append(Ingredient.query.get(86))

  drink36=Drink.query.get(36)
  drink36.ingredients.append(Ingredient.query.get(405))

  drink36.ingredients.append(Ingredient.query.get(168))

  drink36.ingredients.append(Ingredient.query.get(264))

  drink37=Drink.query.get(37)
  drink37.ingredients.append(Ingredient.query.get(359))

  drink37.ingredients.append(Ingredient.query.get(263))

  drink37.ingredients.append(Ingredient.query.get(429))

  drink37.ingredients.append(Ingredient.query.get(175))

  drink37.ingredients.append(Ingredient.query.get(241))

  drink38=Drink.query.get(38)
  drink38.ingredients.append(Ingredient.query.get(282))

  drink38.ingredients.append(Ingredient.query.get(59))

  drink38.ingredients.append(Ingredient.query.get(316))

  drink38.ingredients.append(Ingredient.query.get(352))

  drink38.ingredients.append(Ingredient.query.get(138))

  drink39=Drink.query.get(39)
  drink39.ingredients.append(Ingredient.query.get(381))

  drink39.ingredients.append(Ingredient.query.get(263))

  drink39.ingredients.append(Ingredient.query.get(316))

  drink39.ingredients.append(Ingredient.query.get(352))

  drink40=Drink.query.get(40)
  drink40.ingredients.append(Ingredient.query.get(381))

  drink40.ingredients.append(Ingredient.query.get(429))

  drink40.ingredients.append(Ingredient.query.get(316))

  drink40.ingredients.append(Ingredient.query.get(263))

  drink40.ingredients.append(Ingredient.query.get(114))

  drink40.ingredients.append(Ingredient.query.get(109))

  drink41=Drink.query.get(41)
  drink41.ingredients.append(Ingredient.query.get(148))

  drink41.ingredients.append(Ingredient.query.get(92))

  drink42=Drink.query.get(42)
  drink42.ingredients.append(Ingredient.query.get(92))

  drink42.ingredients.append(Ingredient.query.get(337))

  drink43=Drink.query.get(43)
  drink43.ingredients.append(Ingredient.query.get(6))

  drink43.ingredients.append(Ingredient.query.get(129))

  drink43.ingredients.append(Ingredient.query.get(263))

  drink44=Drink.query.get(44)
  drink44.ingredients.append(Ingredient.query.get(20))

  drink44.ingredients.append(Ingredient.query.get(203))

  drink44.ingredients.append(Ingredient.query.get(241))

  drink45=Drink.query.get(45)
  drink45.ingredients.append(Ingredient.query.get(216))

  drink45.ingredients.append(Ingredient.query.get(203))

  drink45.ingredients.append(Ingredient.query.get(398))

  drink46=Drink.query.get(46)
  drink46.ingredients.append(Ingredient.query.get(42))

  drink46.ingredients.append(Ingredient.query.get(214))

  drink46.ingredients.append(Ingredient.query.get(254))

  drink47=Drink.query.get(47)
  drink47.ingredients.append(Ingredient.query.get(245))

  drink47.ingredients.append(Ingredient.query.get(339))

  drink47.ingredients.append(Ingredient.query.get(316))

  drink47.ingredients.append(Ingredient.query.get(436))

  drink47.ingredients.append(Ingredient.query.get(318))

  drink47.ingredients.append(Ingredient.query.get(287))

  drink48=Drink.query.get(48)
  drink48.ingredients.append(Ingredient.query.get(461))

  drink48.ingredients.append(Ingredient.query.get(316))

  drink49=Drink.query.get(49)
  drink49.ingredients.append(Ingredient.query.get(128))

  drink49.ingredients.append(Ingredient.query.get(17))

  drink50=Drink.query.get(50)
  drink50.ingredients.append(Ingredient.query.get(218))

  drink50.ingredients.append(Ingredient.query.get(442))

  drink50.ingredients.append(Ingredient.query.get(430))

  drink50.ingredients.append(Ingredient.query.get(275))

  drink51=Drink.query.get(51)
  drink51.ingredients.append(Ingredient.query.get(203))

  drink51.ingredients.append(Ingredient.query.get(436))

  drink51.ingredients.append(Ingredient.query.get(175))

  drink51.ingredients.append(Ingredient.query.get(116))

  drink52=Drink.query.get(52)
  drink52.ingredients.append(Ingredient.query.get(425))

  drink52.ingredients.append(Ingredient.query.get(442))

  drink52.ingredients.append(Ingredient.query.get(449))

  drink52.ingredients.append(Ingredient.query.get(263))

  drink52.ingredients.append(Ingredient.query.get(424))

  drink52.ingredients.append(Ingredient.query.get(398))

  drink53=Drink.query.get(53)
  drink53.ingredients.append(Ingredient.query.get(461))

  drink53.ingredients.append(Ingredient.query.get(138))

  drink53.ingredients.append(Ingredient.query.get(218))

  drink54=Drink.query.get(54)
  drink54.ingredients.append(Ingredient.query.get(203))

  drink54.ingredients.append(Ingredient.query.get(263))

  drink54.ingredients.append(Ingredient.query.get(430))

  drink54.ingredients.append(Ingredient.query.get(365))

  drink54.ingredients.append(Ingredient.query.get(175))

  drink54.ingredients.append(Ingredient.query.get(86))

  drink55=Drink.query.get(55)
  drink55.ingredients.append(Ingredient.query.get(203))

  drink55.ingredients.append(Ingredient.query.get(263))

  drink55.ingredients.append(Ingredient.query.get(430))

  drink55.ingredients.append(Ingredient.query.get(48))

  drink56=Drink.query.get(56)
  drink56.ingredients.append(Ingredient.query.get(203))

  drink56.ingredients.append(Ingredient.query.get(435))

  drink56.ingredients.append(Ingredient.query.get(316))

  drink56.ingredients.append(Ingredient.query.get(430))

  drink57=Drink.query.get(57)
  drink57.ingredients.append(Ingredient.query.get(40))

  drink57.ingredients.append(Ingredient.query.get(275))

  drink57.ingredients.append(Ingredient.query.get(430))

  drink57.ingredients.append(Ingredient.query.get(224))

  drink58=Drink.query.get(58)
  drink58.ingredients.append(Ingredient.query.get(200))

  drink58.ingredients.append(Ingredient.query.get(449))

  drink58.ingredients.append(Ingredient.query.get(316))

  drink58.ingredients.append(Ingredient.query.get(141))

  drink59=Drink.query.get(59)
  drink59.ingredients.append(Ingredient.query.get(461))

  drink59.ingredients.append(Ingredient.query.get(337))

  drink59.ingredients.append(Ingredient.query.get(138))

  drink59.ingredients.append(Ingredient.query.get(218))

  drink60=Drink.query.get(60)
  drink60.ingredients.append(Ingredient.query.get(442))

  drink60.ingredients.append(Ingredient.query.get(316))

  drink60.ingredients.append(Ingredient.query.get(224))

  drink60.ingredients.append(Ingredient.query.get(318))

  drink60.ingredients.append(Ingredient.query.get(287))

  drink61=Drink.query.get(61)
  drink61.ingredients.append(Ingredient.query.get(396))

  drink61.ingredients.append(Ingredient.query.get(171))

  drink61.ingredients.append(Ingredient.query.get(288))

  drink61.ingredients.append(Ingredient.query.get(20))

  drink61.ingredients.append(Ingredient.query.get(287))

  drink62=Drink.query.get(62)
  drink62.ingredients.append(Ingredient.query.get(136))

  drink62.ingredients.append(Ingredient.query.get(270))

  drink63=Drink.query.get(63)
  drink63.ingredients.append(Ingredient.query.get(203))

  drink63.ingredients.append(Ingredient.query.get(275))

  drink63.ingredients.append(Ingredient.query.get(430))

  drink63.ingredients.append(Ingredient.query.get(274))

  drink64=Drink.query.get(64)
  drink64.ingredients.append(Ingredient.query.get(73))

  drink64.ingredients.append(Ingredient.query.get(176))

  drink64.ingredients.append(Ingredient.query.get(364))

  drink65=Drink.query.get(65)
  drink65.ingredients.append(Ingredient.query.get(461))

  drink65.ingredients.append(Ingredient.query.get(267))

  drink65.ingredients.append(Ingredient.query.get(241))

  drink66=Drink.query.get(66)
  drink66.ingredients.append(Ingredient.query.get(128))

  drink66.ingredients.append(Ingredient.query.get(129))

  drink66.ingredients.append(Ingredient.query.get(263))

  drink67=Drink.query.get(67)
  drink67.ingredients.append(Ingredient.query.get(92))

  drink67.ingredients.append(Ingredient.query.get(429))

  drink67.ingredients.append(Ingredient.query.get(20))

  drink67.ingredients.append(Ingredient.query.get(264))

  drink67.ingredients.append(Ingredient.query.get(128))

  drink68=Drink.query.get(68)
  drink68.ingredients.append(Ingredient.query.get(405))

  drink68.ingredients.append(Ingredient.query.get(17))

  drink69=Drink.query.get(69)
  drink69.ingredients.append(Ingredient.query.get(394))

  drink69.ingredients.append(Ingredient.query.get(218))

  drink69.ingredients.append(Ingredient.query.get(288))

  drink69.ingredients.append(Ingredient.query.get(275))

  drink70=Drink.query.get(70)
  drink70.ingredients.append(Ingredient.query.get(271))

  drink70.ingredients.append(Ingredient.query.get(351))

  drink70.ingredients.append(Ingredient.query.get(275))

  drink70.ingredients.append(Ingredient.query.get(429))
  db.session.commit()



# Drink_ingredient(drinkId= ingredientId=)

def undo_drink_ingredients():
  db.session.execute('TRUNCATE drink_ingredients RESTART IDENTITY CASCADE')
  db.session.commit()
