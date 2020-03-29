from flask import Blueprint, abort, jsonify, request

import controller

blueprint = Blueprint("api", __name__)


@blueprint.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@blueprint.route("/market")
def market():
    # TODO Handle timestamp
    if "id" in request.args:
        market_id = request.args.get("id")
        result = controller.get_market(market_id)

        if result is not None:
            return result.to_dict()

        abort(404)

    if "postcode" in request.args:
        postcode = request.args.get("postcode")
        results = [result.to_dict() for result in controller.get_postcode(postcode)]

        return jsonify(results)

    abort(400)


@blueprint.route("/visit")
def visit():
    if "market_id" in request.args:
        market_id = request.args.get("market_id")
        results = [result.to_dict() for result in controller.get_visits(market_id)]

        return jsonify(results)

    abort(400)


@blueprint.route("/visit/<int:market_id>/<int:timestamp>", methods=["GET", "POST"])
def visit_time(market_id: int, timestamp: int):
    if request.method == "GET":
        results = [result.to_dict() for result in controller.get_visits_time(market_id, timestamp)]
        return jsonify(results)

    if request.method == "POST":
        result = controller.add_visit(market_id, timestamp)
        if result is not None:
            return result.to_dict()

    abort(404)
