from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()], description='Please enter your full name.')
    email = EmailField('Email',validators=[DataRequired(), Email()], description='Please enter your e-mail address.')
    subject = StringField('Subject',validators=[DataRequired()], description='Please enter the subject for you message.')
    message = TextAreaField('Message',validators=[DataRequired()], description='Please enter the message you would like to send.')