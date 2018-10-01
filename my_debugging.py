from flask import Flask, request, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' # Can be whatever for us, for now; this is what 'seeds' the CSRF protection
app.debug=True

API_KEY = 'f37d2a49b946d808bffe304d318c2ab'

class = weatherForm(FlaskForm):
    zip_code = IntegerField("Enter a US zipcode", validators=[Required()])
    submit = SubmitField("Submit")

    def zip_len(self, field):
        if len(str(field.data)) != 5:
            raise ValidationError('Please enter a 5 digit zipcode')

@app.route('/zipcode', methods=["GET","POST"])
def zip_form():
    form = weatherForm()
    if form.validate_on_submit():
        my_zip = request.args.get('')
        my_url = 'https://itunes.apple.com/search'
        my_params = {}
        my_params['term'] = artist
        my_request = requests.get(my_url, params = my_params)
        harrison = json.loads(my_request.text)
        #call API
        #get response
        #return template with response fields
    flash(form.errors)
    return render_template('weather_form.html'), form = form

