from flask import Blueprint, abort, jsonify, request

import controller

blueprint = Blueprint("api", __name__)


@blueprint.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@blueprint.route("/market/<int:market_id>")
def market(market_id: int):
    result = controller.get_market(market_id)
    if result is not None:
        return result.to_dict()

    abort(404)


@blueprint.route("/visit/<int:market_id>")
def visit(market_id: int):
    results = [result.to_dict() for result in controller.get_visits(market_id)]
    return jsonify(results)


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


@blueprint.route("/postcode/<string:code>")
def postcode(code: str):
    results = [result.to_dict() for result in controller.get_postcode(code)]

    return jsonify(results)


@blueprint.route("/postcode/<string:code>/<int:timestamp>")
def postcode_time(code: str, timestamp: int):
    abort(501)
