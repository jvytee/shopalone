from flask import Flask, abort, jsonify, request

import database
import controller

app = Flask(__name__)
app.teardown_appcontext(database.close_session)
app.cli.add_command(database.init_db)


@app.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@app.route("/market/<int:market_id>")
def market(market_id: int):
    result = controller.get_market(market_id)
    if result is not None:
        return result.to_dict()

    abort(404)


@app.route("/visit/<int:market_id>")
def visit(market_id: int):
    results = [result.to_dict() for result in controller.get_visits(market_id)]
    return jsonify(results)


@app.route("/visit/<int:market_id>/<int:timestamp>", methods=["GET", "POST"])
def visit_time(market_id: int, timestamp: int):
    if request.method == "GET":
        results = [result.to_dict() for result in controller.get_visits_at(market_id, timestamp)]
        return jsonify(results)

    if request.method == "POST":
        result = controller.add_visit(market_id, timestamp)
        if result is not None:
            return result.to_dict()

        abort(404)


@app.route("/postcode/<string:code>")
def postcode(code: str):
    return code


@app.route("/postcode/<string:code>/<int:timestamp>")
def postcode_time(code: str, timestamp: int):
    return f"{code} at {timestamp}"
