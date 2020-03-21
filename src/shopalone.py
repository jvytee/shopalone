from flask import Flask, abort, jsonify, request

import database
from model import Node

app = Flask(__name__)


@app.route('/')
def index():
    return 'shopalone'


@app.route('/market/id/<int:key>', methods=['GET', 'POST'])
def market_id(key: int):
    if request.method == 'GET':
        session = database.get_session()
        nodes = session.query(Node).filter(Node.id == key).all()

        if len(nodes):
            return jsonify([node.tags for node in nodes])

        abort(404)

    abort(501)


@app.route('/market/postcode/<string:code>')
@app.route('/market/postcode/<string:code>/<int:timestamp>')
def postcode_timestamp(code: str, timestamp: int = None):
    if timestamp is None:
        return code

    return f'{code} at {timestamp}'
