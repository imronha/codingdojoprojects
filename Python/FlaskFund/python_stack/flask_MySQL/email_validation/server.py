from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = "dkajsd"
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    print all_emails
    return render_template('index.html', all_emails=emails)

@app.route('/create', methods=['POST'])
def create_email():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        query = "INSERT INTO email (name, created_at, updated_at) VALUES (:name, NOW(), NOW())"
        data = {'name': request.form['email']}
        email_entered = mysql.query_db(query, data)
        flash("Success!")
        return render_template('success.html')
    # user_email = request.form['email']
    # user_query = "SELECT * FROM email WHERE email.name = :name"
    # query_data = {'name': user_email}
    # email = mysql.query_db(user_query,query_data)
    # print user_email
    # print user_query
    # print query_data
    # print email
    # # if email[0]['name'] == email:
    # #     print "Email is valid!"
    # # else:
    # #     print "Email is not valid"
    return redirect('/')


app.run(debug=True)
