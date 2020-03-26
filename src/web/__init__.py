from flask import Blueprint, render_template

blue = Blueprint("web", __name__, static_folder="static", template_folder="templates")

@blue.route("/")
def index():
    return render_template("index.html")
