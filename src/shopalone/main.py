"""Main entrypoint for the shopalone flask app.
Registers teardown handler, CLI commands and the api and web blueprints.

Middleware (e.g. gunicorn) must load the app as shopalone.main:app.
"""

from flask import Flask, redirect, url_for

from . import api, database, web


app = Flask(__name__)
app.teardown_appcontext(database.close_session)
app.cli.add_command(database.init_db)

app.register_blueprint(api.blueprint, url_prefix="/api")
app.register_blueprint(web.blueprint, url_prefix="/web")


@app.route("/")
def index():
    return redirect(url_for("web.index"), 303)
