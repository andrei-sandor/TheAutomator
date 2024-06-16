from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from passwordAutomator import *

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)


# Models
class Profile(db.Model):
    # Id : Field which stores unique id for every row in
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"


# function to render index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pass', methods=['POST', 'GET'])
def password():
    #if request.method == 'POST':
    minlength = request.form.get("minlength")
    maxlength = request.form.get("maxlength")
    upper = request.form.get("upper")
    lower = request.form.get("lower")
    numbers = request.form.get("numbers")
    special = request.form.get("special")
    password = None

    if minlength is not None and maxlength is not None and upper is not None and lower is not None and numbers is not None and special is not None:
        password = automatePasssword(True,(minlength),(maxlength), (numbers),True, (upper),(lower),(special),True)
    return render_template('pass.html',minlength=minlength,
                                    maxlength=maxlength,
                                    upper=upper,
                                    lower=lower,
                                    numbers=numbers,
                                    special=special,
                                    password=password)

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/excel')
def excel():
    return render_template('excel.html')

@app.route('/currency')
def currency():
    return render_template('currency.html')


@app.route('/form')
def add_data():
    return render_template('form.html')


# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
    # In this function we will input data from the
    # form page and store it in our database. Remember
    # that inside the get the name should exactly be the same
    # as that in the html input fields
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")

    # create an object of the Profile class of models and
    # store data as a row in our datatable
    if first_name != '' and last_name != '' and age is not None:
        p = Profile(first_name=first_name, last_name=last_name, age=age)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')


@app.route('/delete/<int:id>')
def erase(id):
    # deletes the data on the basis of unique id and
    # directs to home page
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()
