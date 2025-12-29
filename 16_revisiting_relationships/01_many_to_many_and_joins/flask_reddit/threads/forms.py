"""
"""
from flask_reddit.threads import constants as THREAD
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, URL, Length

class SubmitForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    text = TextAreaField('Body text') # [Length(min=5, max=THREAD.MAX_BODY)]
    link = StringField('Link', [URL(require_tld=True,
        message="That is not a valid link url!")])
