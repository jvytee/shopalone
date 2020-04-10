from dateutil import parser
from flask import Blueprint, abort, render_template, request, Response

import controller
from web import plotter

blueprint = Blueprint("web", __name__, static_folder="static", template_folder="templates")


@blueprint.route("/")
def index():
    markets = None
    if "postcode" in request.args:
        markets = controller.get_postcode(request.args.get("postcode"))

    return render_template("index.html", markets=markets)


@blueprint.route("/visit", methods=["GET", "POST"])
def visit():
    if request.method == "GET":
        market_id = request.args.get("market_id")

        if market_id is not None:
            market = controller.get_market(market_id)
            visits = controller.get_visits(market_id)

            return render_template("visit.html", market=market, visits=visits)

    if request.method == "POST":
        market_id = request.form.get("market_id")
        timestamp = request.form.get("timestamp")

        if market_id is not None and timestamp is not None:
            tstamp_parsed = parser.parse(timestamp).timestamp()
            controller.add_visit(market_id, int(tstamp_parsed))

            market = controller.get_market(market_id)
            visits = controller.get_visits(market_id)

            return render_template("visit.html", market=market, visits=visits, market_id=market_id, timestamp=timestamp)

    abort(404)


@blueprint.route("/plot")
def plot():
    market_id = request.args.get("market_id")

    if market_id is not None:
        visits = controller.get_visits(market_id)
        image = plotter.plot_visits(visits)

        return Response(image.getvalue(), mimetype="image/png")
