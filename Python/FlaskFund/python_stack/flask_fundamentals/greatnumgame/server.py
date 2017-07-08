from flask import Flask, render_template, redirect, request, session

app= Flask(__name__)
app.secret_key = "numgamekey"

import random

@app.route('/')
def index():
    if "number" not in session:
        session["number"] = random.randrange(0,101)
    return render_template("index.html")

@app.route('/number', methods=['POST'])
def guess():
    if int(request.form['guess']) == session["number"]:
        return render_template('win.html')
    elif int(request.form['guess']) > session["number"]:
        return render_template('high.html')
    elif int(request.form['guess']) < session["number"]:
        return render_template('low.html')
    return redirect('/')

@app.route('/replay', methods=['POST'])
def replay():
    session["number"] = random.randrange(0,101)
    return redirect('/')

app.run(debug=True)
