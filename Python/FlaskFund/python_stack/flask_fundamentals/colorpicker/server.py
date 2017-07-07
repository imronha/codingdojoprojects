from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET'])
def rgb():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    return redirect('/')

app.run(debug=True)
