from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = "dkajsd"
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    query_response = mysql.query_db(query)
    print query_response
    return render_template('users.html', all_users = query_response)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=["POST"])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:f_name, :l_name, :email, NOW(), NOW())"
    data = {
        "f_name": request.form['first_name'],
        "l_name": request.form['last_name'],
        "email": request.form['email']
    }
    query_response = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
