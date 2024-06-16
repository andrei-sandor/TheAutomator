from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from passwordAutomator import *
from emailAutomator import *
from formAutomator import *
#from excelAutomator import *
from currencyAutomator import *

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



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

@app.route('/email', methods=["POST", "GET"])
def email():
    staticEmail = request.form.get("staticEmail")
    inputPassword = request.form.get("inputPassword")
    staticEmail2 = request.form.get("staticEmail2")
    message = request.form.get("message")
    if staticEmail is not None and inputPassword is not None and staticEmail2 is not None:
        automateMessage(staticEmail,inputPassword,staticEmail2)
    return render_template('email.html', staticEmail=staticEmail,
                               inputPassword=inputPassword,
                               staticEmail2=staticEmail2,
                               message=message)

@app.route('/excel', methods=["POST", "GET"])
def excel():
    formFile = request.form.get("formFile")
    exampleCheck1 = request.form.get("exampleCheck1")
    exampleCheck2 = request.form.get("exampleCheck2")
    exampleCheck3 = request.form.get("exampleCheck3")
    exampleCheck4 = request.form.get("exampleCheck4")
    exampleCheck5 = request.form.get("exampleCheck5")
    exampleCheck6 = request.form.get("exampleCheck6")
    exampleCheck7 = request.form.get("exampleCheck7")

    if formFile is not None and exampleCheck1 is not None and exampleCheck2 is not None and exampleCheck3 is not None and exampleCheck4 is not None and exampleCheck5 is not None and exampleCheck6 is not None and exampleCheck7 is not None:
        done = "Done"
        #excel_automator(formFile,exampleCheck1,exampleCheck2,exampleCheck3,exampleCheck4,exampleCheck5,exampleCheck6,False,exampleCheck7)
    return render_template('excel.html')

@app.route('/currency', methods=["POST", "GET"])
def currency():
    fromCurrency = request.form.get("fromCurrency")
    toCurrency = request.form.get("toCurrency")
    result = None
    #if fromCurrency is not None and toCurrency is not None:
        #result = currencies_automator(fromCurrency,toCurrency)
    return render_template('currency.html',fromCurrency=fromCurrency,
                                         toCurrency=result)


@app.route('/form', methods=["POST", "GET"])
def add_data():
    websiteForm = request.form.get("websiteForm")
    browser = request.form.get("browser")
    name = request.form.get("name")
    studentNumber = request.form.get("studentNumber")
    emailForm = request.form.get("emailForm")
    phone = request.form.get("phone")
    courseNumber = request.form.get("courseNumber")
    semester = request.form.get("semester")
    program = request.form.get("program")
    message = request.form.get("message")

    if websiteForm is not None and browser is not None and name is not None and studentNumber is not None and emailForm is not None and phone is not None and courseNumber is not None and semester is not None and program is not None:
        form_automator(websiteForm,browser,name,studentNumber,phone,courseNumber,semester,program)
    return render_template('form.html', websiteForm=websiteForm,
                           browser=browser,
                           name=name,
                           studentNumber=studentNumber,
                           emailForm=emailForm,
                           phone=phone,
                           courseNumber=courseNumber,
                           semester=semester,
                           program=program,
                           message=message)


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

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
@app.route('/delete/<int:id>')
def erase(id):
    data = Profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')




    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

if __name__ == '__main__':
    app.run()