from flask import Flask, render_template, request, redirect, session, flash
print __name__
app = Flask(__name__)

app.secret_key = "ThisIsSuperSecret"

@app.route('/')
def index():
	if "wishlist" not in session:
		session["wishlist"] = []
	return render_template('index.html')

@app.route('/wishlists', methods=["POST"])
def additem():
	errors = False
	if len(request.form['item'])<4:
		flash("Field must be at least four characters long")
		errors = True
	if not errors:
		session["wishlist"].append(request.form["item"])
	return redirect('/')

app.run(debug=True)
