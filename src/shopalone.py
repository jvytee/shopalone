from flask import Flask, redirect, url_for


import database
import api
import web

app = Flask(__name__)
app.teardown_appcontext(database.close_session)
app.cli.add_command(database.init_db)

app.register_blueprint(api.blueprint, url_prefix="/api")
app.register_blueprint(web.blueprint, url_prefix="/web")


@app.route("/")
def index():
    return redirect(url_for("web.index"), 303)
