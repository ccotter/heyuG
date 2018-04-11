import flask
from flask import render_template
import json

import heyu

app = flask.Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/css/<css>.css")
def serve_css(css):
    print("Serving " + css)
    return flask.send_from_directory("css", css + ".css")

@app.route("/heyu/status/")
def handle_status():
    try:
        status = heyu.get_status()
        return status
    except:
        logger.error("get_status failed")
    return "Command failed!"

@app.route("/heyu/commands/<command>", methods=["POST"])
def handle_command(command):
    print("Got command " + command)
    return json.dumps({})
