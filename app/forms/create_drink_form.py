from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateDrinkForm(FlaskForm):
  authorId = IntegerField("authorId", [DataRequired()])
  photo_url = StringField("photo_url", [DataRequired()])
  name = StringField("name", [DataRequired()])
  instructions = StringField("instructions", [DataRequired()])
  ingredients = StringField("ingredients", [DataRequired()])
  submit = SubmitField("Submit")
