from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'shopalone'

@app.route('/market/id/<int:key>', methods=['GET', 'POST'])
def market_id(key: int):
    return str(key)

@app.route('/market/postcode/<string:code>')
def postcode(code: str):
    return code

@app.route('/market/postcode/<string:code>/<int:timestamp>')
def postcode_timestamp(code: str, timestamp: int):
    return f'{code} at {timestamp}'
