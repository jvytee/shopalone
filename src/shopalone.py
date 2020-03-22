from flask import Flask, abort, jsonify, request

import database
import controller

app = Flask(__name__)
app.teardown_appcontext(database.close_session)


@app.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@app.route("/market/<int:market_id>")
def market(market_id: int):
    result = controller.get_market(market_id)
    if result is not None:
        return result

    abort(404)


@app.route("/visit/<int:market_id>")
def visit(market_id: int):
    return jsonify(market_id)


@app.route("/visit/<int:market_id>/<int:timestamp>", methods=["GET", "POST"])
def visit_time(market_id: int, timestamp: int):
    if request.method == "GET":
        abort(501)

    if request.method == "POST":
        visit = Visit(node_id=market_id, way_id=market_id, tstamp=timestamp, weight=1)
        return f"{market_id} at {timestamp}"


@app.route("/postcode/<string:code>")
def postcode(code: str):
    return code


@app.route("/postcode/<string:code>/<int:timestamp>")
def postcode_time(code: str, timestamp: int):
    return f"{code} at {timestamp}"
