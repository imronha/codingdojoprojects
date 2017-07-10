from flask import Flask, render_template, redirect, request, session, flash
import re

app= Flask(__name__)
app.secret_key = "regformkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    full_name = request.form['first_name'] + request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirmpw = request.form['confirmpw']
    errors = False
    if len(request.form["first_name"]) == 0:
        flash("You must include a first name!")
        errors = True
    if len(request.form["last_name"]) == 0:
        flash("You must include a last name!")
        errors = True
    if len(request.form["last_name"])!= 0 and len(request.form["first_name"]) !=0 and full_name.isalpha()==False:
            flash("Your name cannot contain any numbers or special characters.")
            errors = True
        # <-- code below also works -->
        # for char in full_name:
        #     nums = ['0','1','2','3','4','5','6','7','8','9']
        #     if char in nums:
        #         flash("Your name cannot contain any numbers.")
        #         errors = True
        #         break
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
    #elif add uppcase & number req here
    elif password != confirmpw:
        flash("Your password confirmation must be the same as your password!")
        errors = True
    if not errors:
        flash("Thank you for submitting your information")
    return render_template("index.html")

app.run(debug=True)
