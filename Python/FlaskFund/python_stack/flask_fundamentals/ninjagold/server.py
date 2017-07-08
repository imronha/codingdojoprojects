from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ninjagoldkey"

import random

@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    # print request.form['building']
    if request.form['building'] == 'farm':
        earned = random.randrange(10,21)
        session["gold"] += earned
        session["activities"].append("You earned "+str(earned)+" gold from the farm!")
    elif request.form['building'] == 'cave':
        earned = random.randrange(5,11)
        session["gold"] += earned
        session["activities"].append("You earned "+str(earned)+" gold from the cave!")
    elif request.form['building'] == 'house':
        earned = random.randrange(2,6)
        session["gold"] += earned
        session["activities"].append("You earned "+str(earned)+" gold from the house!")
    elif request.form['building'] == 'casino':
        win = random.randrange(1,11)
        if win>0 and win<6:
            earned = random.randrange(0,51)
            session["gold"] += earned
            session["activities"].append("You earned "+str(earned)+" gold from the casino!")
        else:
            lost = random.randrange(0,51)
            session["gold"] -= lost
            session["activities"].append("You lost "+str(lost)+" gold from the casino...")
            # session["gold"] -= random.randrange(0,51)
    # print session["activities"]

    return redirect('/')

app.run(debug=True)
