import subprocess
import logging

logger = logging.getLogger(__name__)

def _run(args):
    args = ["sudo"] + args
    logger.info("Running cmd: {}".format(args))
    print("Running cmd: {}".format(args))
    return subprocess.check_output(args)

def get_status():
    args = ["heyu", "info"]
    return _run(args)

def all_on():
    args = ["heyu", "allon", "A"]
    return _run(args)

def all_off():
    args = ["heyu", "alloff", "A"]
    return _run(args)

def turn_on(hu):
    args = ["heyu", "on", hu]
    return _run(args)

def turn_off(hu):
    args = ["heyu", "off", hu]
    return _run(args)
