from flask import Flask, abort, jsonify, request

import database
import util
from model import Node, Way, Visit

app = Flask(__name__)
app.teardown_appcontext(database.close_session)


@app.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@app.route("/market/<int:market_id>")
def market(market_id: int):
    session = database.get_session()

    node = session.query(Node).filter(Node.id == market_id).first()
    if node is not None:
        return {"id": node.id, "tags": node.tags, "location": util.to_list(node.geom)}

    way = session.query(Way).filter(Way.id == market_id).first()
    if way is not None:
        return {"id": way.id, "tags": way.tags, "location": list()}

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
