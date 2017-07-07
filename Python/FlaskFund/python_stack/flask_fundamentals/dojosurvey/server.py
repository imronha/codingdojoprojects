from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def submit_survey():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name, location, language, comment
    return render_template("results.html", sub_name=name, sub_loc=location, sub_lang=language, sub_com=comment)
    return redirect('/results.html')

app.run(debug=True)
