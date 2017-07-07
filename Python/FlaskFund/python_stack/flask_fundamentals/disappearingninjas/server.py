from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninjas/<color>')
def single_ninja(color):
    if color == "red" or color == "blue" or color =="orange" or color == "purple":
        return render_template(color+".html")
    else:
        return render_template("notapril.html")

app.run(debug=True)
