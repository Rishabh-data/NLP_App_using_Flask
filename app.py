from flask import Flask, render_template,request,redirect,session
from db import Database
import api
# Render_template loads HTML files & displays to user. Request is used to receive the data
# Redirect is used for redirecting from one route to another


app  = Flask(__name__)

dbo = Database()

@app.route('/') #Whenever a user presses '/' after out website url and then enter the index function code will execute
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html',message = "Registration successful. Kindly login to proceed")

    else:
        return render_template('register.html', message="Email already Exists")

@app.route('/perform_login',methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email, password)
    if response:
        session['logged_in']=1
        return redirect('/profile')
    else:
        return render_template('login.html',message = 'Incorrect email/password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods = ['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)

        return render_template('ner.html',response = response)
    else:
        return redirect('/')



app.run(debug = True) # Debug ensures that Any changes made won't require code re-run, just refresh the open flask app


