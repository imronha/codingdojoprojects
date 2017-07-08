from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key="surveryvalidation"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def submit_survey():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    errors = False
    if len(name)==0:
        flash("Please enter a name!")
        errors = True
    if len(comment)>120:
        flash("Please limit comments to 120 characters or less :)")
        errors = True
    elif len(comment)==0:
        flash("Please enter some comments!")
        errors = True
    if not errors:
        return render_template("results.html", sub_name=name, sub_loc=location, sub_lang=language, sub_com=comment)

    # print name, location, language, comment
    return redirect('/')

app.run(debug=True)
