from wtforms import StringField, PasswordField, SubmitField, Form, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length


class SaveTripForm(Form):
    """
    Form for users to login
    """
    from_ = StringField('Origin', id="origin")
    to_ = StringField('Destination', id="destination")
    distance = StringField('Distance', id='distance')
    time = StringField('Time', id='time')
    total = StringField('Trip Cost', id='cost')
    ttype = RadioField('Trip Category', choices=[
        ('corp','Corporate'),
        ('indv','Individual')])
    vtype = SelectField('Vehicle Type', choices=[
        ('b', 'Basic'),
        ('c', 'Comfort'),
        ('cp', 'Comfort Plus'),
        ('g', 'Goods'),
        ('boda', 'Boda Boda')], id='vtype')
    submit = SubmitField('Report Issue')