from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from firstapp.models import User

class AddUser(FlaskForm):
    name = StringField(label='Name of the Person taken Debt', validators=[Length(min=5,max=50), DataRequired()])
    address = StringField(label='Address', validators=[Length(min=7,max=100), DataRequired()])
    submit = SubmitField(label='Add user to the accounts')