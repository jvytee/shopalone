from flask import Flask, abort, jsonify, request

import database
import api
import web

app = Flask(__name__)
app.teardown_appcontext(database.close_session)
app.cli.add_command(database.init_db)

app.register_blueprint(api.blue)
app.register_blueprint(web.blue, url_prefix="/web")
