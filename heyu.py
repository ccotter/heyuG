import subprocess
import logging

logger = logging.getLogger(__name__)

def _run(args):
    args = ["sudo"] + args
    logger.info("Running cmd: {}".format(args))
    return subprocess.check_output(args)

def get_status():
    args = ["heyu", "info"]
    return _run(args)
