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

        node = session.query(Node).filter(Node.id == key).first()
        if node is not None:
            return {"id": node.id, "tags": node.tags, "location": util.to_list(node.geom)}

        way = session.query(Way).filter(Way.id == key).first()
        if way is not None:
            return {"id": way.id, "tags": way.tags, "location": list()}

        abort(404)
    else:
        abort(501)


@app.route("/market/postcode/<string:code>")
@app.route("/market/postcode/<string:code>/<int:timestamp>")
def postcode_timestamp(code: str, timestamp: int = None):
    if timestamp is None:
        return code

    return f"{code} at {timestamp}"
