from flask import Blueprint, g, render_template, request, url_for, redirect

mod = Blueprint("general", __name__)

@mod.route("/")
def home():
    return render_template("home.html")
