import flask
from flask import render_template
import json
import logging

logger = logging.getLogger(__name__)

if False:
    import heyu
else:
    import heyu_mock as heyu

app = flask.Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/css/<css>.css")
def serve_css(css):
    print("Serving " + css)
    return flask.send_from_directory("css", css + ".css")

@app.route("/heyu/status")
def handle_status():
    try:
        status = heyu.get_status()
        return status
    except:
        logger.error("get_status failed")
        raise
    return "Command failed!"

@app.route("/heyu/commands/<command>", methods=["POST"])
def handle_command(command):
    print("Got command " + command)
    if command.startswith("all_"):
        if command == "all_on":
            heyu.all_on()
        else:
            heyu.all_off()
    elif "_" in command:
        (hu, on_or_off) = command.split("_")
        if on_or_off == "on":
            heyu.turn_on(hu)
        else:
            heyu.turn_off(hu)

    return json.dumps({})
