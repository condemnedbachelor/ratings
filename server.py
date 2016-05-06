"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, make_response

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    flash('hi')
    return render_template("homepage.html")

@app.route("/users")
def user_list():
	"""Show list of users."""
	users = User.query.all()
	flash("it's working!")
	return render_template("user_list.html", users=users)

@app.route("/sign_in")
def sign_in():
	"""Allows user to sign in, or creates new user if user is not in db."""
	flash('hi')
	# users = User.query.all()
	return render_template("homepage.html")

# @app.route("/create_new")
# def user_list():
# 	"""Creates new user if user is not in db."""

# 	return render_template(".html", users=users)

@app.route("/user_auth", methods=['POST'])
def user_auth():
	"""Allows user to sign in, or creates new user if user is not in db."""
	username = request.form.get('email-field')
	password = request.form.get('pass-field')

	# User.query.filter(User.email == 

	if username:
		User.query.filter_by(email = username).first()
		 #If username exists in db, sign in. 
		 # Else, create user in db.
		flash("Logged in as %s" % username)
		password = User.query.filter_by(password = password).first()
		if password:
			session['current user'] = username
			flash("pw success Logged in as %s" % username)
		# db.session.commit()
			return render_template("homepage.html")
	# else:
	# 	flash("Please create an account. You will be redirected to the sign-up page in exactly 600 milliseconds.")
	# 	return redirect("/create_new")




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
