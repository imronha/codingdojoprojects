from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secrettt"

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
        return render_template("index.html")
    if session["counter"]>=0:
        session["counter"]+=1
        return render_template("index.html")
    # while session["counter"] >=0:
    #     if session["counter"] ==0:
    #         print "if loop"
    #         session["counter"].append()
    #         return render_template("index.html")
    #     else:
    #         print session["counter"],"else loop"
    #         session["counter"]+=1
    #         return redirect('/')

app.run(debug=True)
