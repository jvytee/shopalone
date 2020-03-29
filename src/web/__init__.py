from flask import Blueprint, render_template, request

import controller

blueprint = Blueprint("web", __name__, static_folder="static", template_folder="templates")


@blueprint.route("/")
def index():
    markets = None
    if "postcode" in request.args:
        markets = controller.get_postcode(request.args.get("postcode"))

    return render_template("index.html", markets=markets)
