from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'loginandreg')
app.secret_key = "dkajsd"
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    full_name = request.form['first_name'] + request.form['last_name']
    email = request.form['email']
    password = request.form['pw']
    pwconfirm = request.form['pwconfirm']
    errors = False
    if len(request.form["first_name"]) < 2:
        flash("Your first name must be at least 2 letters long!")
        errors = True
    if len(request.form["last_name"]) < 2:
        flash("Your last name must be at least 2 letters long!")
        errors = True
    if len(request.form["last_name"])<2 and len(request.form["first_name"]) <2 and full_name.isalpha()==False:
            flash("Your name cannot contain any numbers or special characters.")
            errors = True
    if len(email) == 0:
        flash("You must include an email!")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email")
        errors = True
    if len(password) == 0:
        flash("You must include a password!")
        errors = True
    elif len(password) < 8:
        flash("Your password must be at least 8 letters long!")
        errors = True
    elif password != pwconfirm:
        flash("Your password confirmation must be the same as your password!")
        errors = True
    if not errors:
        hashed_pw = md5.new(request.form['pw']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": hashed_pw
        }
        users = mysql.query_db(query, data)
        flash("Thank you for submitting your information")
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT email, password FROM users"
    query_return = mysql.query_db(query)
    pw_entered = md5.new(request.form['pw']).hexdigest()
    # print query_return
    for i in range(0,len(query_return)):
        if query_return[i]['email'] == request.form['email'] and query_return[i]['password'] == pw_entered:
            # print "yasss"
            return render_template('success.html')
    if query_return[i]['email'] != request.form['email']:
        flash("Your email or password was incorrect!")
    return redirect('/')


app.run(debug=True)
