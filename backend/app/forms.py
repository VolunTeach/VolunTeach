from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class MatchForm(FlaskForm):
    """Match form."""
    client_preferences = StringField('Client Preferences: ', [
        DataRequired()])
    tutors = TextField('Tutors: ', [
        DataRequired()])
    submit = SubmitField('Find Matches')