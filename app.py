# The first two lines import Flask and set up a new app

from flask import Flask
app = Flask(__name__)

# 2/ add an import to allow it to use templates
from flask import render_template

# 3/
# In order to use an ORM - to use Python to talk to your database - it takes three steps:
# Add SQLAlchemy to your Flask app
# Make a model, a Python representation of your database table
# Use your model to get stuff

# pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxes.db'
db = SQLAlchemy(app)

class Taxes(db.Model):
  __tablename__ = 'countries'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)

# When you try to visit / on your server, it runs that function and prints out "Your message!"

@app.route("/")
def hello():
  return render_template("home.html")

# Each URL you can visit on your serve is called a route.
# To add another route, we'll just make another @app.route line and another function.
# Notice that I changed the route and the name of the function.
# If you forget to change the name of the function - which is easy, especially if you're cutting and pasting - you'll be setting yourself up for despair (and an error).

@app.route("/countries/")
def list():
  countries = Taxes.query.all()
  return render_template("list.html", countries=countries)

@app.route("/countries/<index>/")
def show(index):
  country = Taxes.query.filter_by(index=index).first() # glitch!
  return render_template("show.html", country=country)

# 2/ then tell our show function to use the template
#@app.route("/countries/info")
#def show():
#  country = Taxes.query.filter_by(index=1).first() # glitch!
#  return render_template("show.html", country_name=country.Country)

  # adjust your app to send a variable to the template -> school_name


# "if someone runs this file with python app.py, run a server."
if __name__ == "__main__":
  app.run(debug=True)

# 0. Install flask in your Terminal if you have not already installed it `pip install flask`
