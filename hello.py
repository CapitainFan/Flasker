from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create a Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

# create a route decaretor
@app.route('/')
def index():
    first_name = "John"
    stuff = "this is <strong>Bald</strong>"
    return render_template("index.html", first_name=first_name,
                           stuff=stuff)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

class NameForm(FlaskForm):
    name = StringField("What your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Succsesfuly")

    return render_template('name.html', name=name, form=form)
