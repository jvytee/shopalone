from dateutil import parser
from flask import Blueprint, abort, jsonify, request

from . import controller

blueprint = Blueprint("api", __name__)


@blueprint.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@blueprint.route("/market")
def market():
    market_id = request.args.get("id")
    if market_id is not None:
        result = controller.get_market(market_id)

        if result is not None:
            return result.to_dict()

        abort(404)

    postcode = request.args.get("postcode")
    if postcode is not None:
        results = [result.to_dict() for result in controller.get_postcode(postcode)]

        return jsonify(results)

    abort(400)


@blueprint.route("/visit", methods=["GET", "POST"])
def visit():
    if request.method == "GET":
        market_id = request.args.get("market_id")

        if market_id is not None:
            results = [result.to_dict() for result in controller.get_visits(market_id)]
            return jsonify(results)

    if request.method == "POST":
        market_id = request.form.get("market_id")
        timestamp = request.form.get("timestamp")

        if market_id is not None and timestamp is not None:
            tstamp_parsed = parser.parse(timestamp).timestamp()
            result = controller.add_visit(market_id, int(tstamp_parsed))

            return result.to_dict()

    abort(404)
