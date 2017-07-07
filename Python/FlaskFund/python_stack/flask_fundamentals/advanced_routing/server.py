from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/users/<username>')
#^ the placeholder (<username>) should match the parameter
# name that is passed to the route handler function
# aka show_user_profile(username)
def show_user_profile(username):
    print username
    return render_template("user.html")

app.run(debug=True)
