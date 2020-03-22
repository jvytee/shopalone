from flask import Flask, abort, jsonify, request

import database
import util
from model import Node, Way

app = Flask(__name__)
app.teardown_appcontext(database.close_session)


@app.route("/")
def index():
    return '<a href="https://github.com/jvytee/shopalone">shopalone</a>'


@app.route("/market/id/<int:key>")
@app.route("/market/id/<int:key>/<int:timestamp>", methods=["GET", "POST"])
def market_id(key: int, timestamp: int = None):
    if timestamp is None:
        session = database.get_session()
        nodes = session.query(Node).filter(Node.id == key).all()
        ways = session.query(Way).filter(Way.id == key).all()

        result_nodes = [{"id": node.id, "tags": node.tags, "location": util.to_list(node.geom)} for node in nodes]
        result_ways = [{"id": way.id, "tags": way.tags, "location": []} for way in ways]
        result = result_nodes + result_ways

        if len(result):
            return jsonify(result)

        abort(404)

    abort(501)


@app.route("/market/postcode/<string:code>")
@app.route("/market/postcode/<string:code>/<int:timestamp>")
def postcode_timestamp(code: str, timestamp: int = None):
    if timestamp is None:
        return code

    return f"{code} at {timestamp}"
