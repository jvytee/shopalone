from flask import Blueprint, render_template

blueprint = Blueprint("web", __name__, static_folder="static", template_folder="templates")


@blueprint.route("/")
def index():
    return render_template("index.html")
