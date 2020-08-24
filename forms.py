from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

    #Username required
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])

    #Email required
    email = StringField('Email', validators=[DataRequired(), Email()])

    #Password required
    password = PasswordField('Password', validators=[DataRequired()])

    #Confirm password
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])

    #Submit required
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):

    #Email required
    email = StringField('Email', validators=[DataRequired(), Email()])

    #Password required
    password = PasswordField('Password', validators=[DataRequired()])

    #Remember info
    remember = BooleanField('Remember Me')

    #Submit button
    submit = SubmitField('Log In')










