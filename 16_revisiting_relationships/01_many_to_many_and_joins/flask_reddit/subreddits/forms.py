"""
"""
from flask_reddit.threads import constants as THREAD
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, URL, Length

class SubmitForm(FlaskForm):
    name = StringField('Name your community!', [DataRequired()])
    desc = TextAreaField('Description of subreddit!', [DataRequired()])
