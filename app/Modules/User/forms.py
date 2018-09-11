from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.Models import User


class LoginForm(Form):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(Form):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=35)])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password', message='Passwords must match')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')