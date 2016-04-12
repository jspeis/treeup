# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (mod_auth)
#from app.mod_auth.controllers import mod_auth as auth_module
from treeup.donations.views import mod as donation_mod

# Register blueprint(s)
app.register_blueprint(donation_mod)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
