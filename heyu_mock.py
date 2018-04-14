import subprocess
import logging

from heyuG.util import parse_status_text

logger = logging.getLogger(__name__)

OFF = 0
ON = 1

class State(object):

    def __init__(self):
        self.hu = dict()
        for hu in range(ord("A"), ord("G")):
            hu = chr(hu)
            self.hu[hu] = dict()
            for i in range(0, 16):
                self.hu[hu][i] = OFF

    def status_as_bitmap(self):
        r = ""
        for i in range(0, 16):
            r += "1" if self.hu["A"][15-i] else "0"
        return r

    def get_status_txt(self):
        return """Last addressed device =       0x
Status of monitored devices = 0x{}
Status of dimmed devices =    0x
""".format(self.status_as_bitmap())

    def get_status(self):
        txt = self.get_status_txt()
        return {
            "txt": txt,
            "devices": parse_status_text(txt)
        }

    def all_on(self):
        for i in range(0, 16):
            self.hu["A"][i] = ON

    def all_off(self):
        for i in range(0, 16):
            self.hu["A"][i] = OFF

    def turn_on(self, hu_input):
        hu = hu_input[0].upper()
        code = int(hu_input[1:]) - 1
        self.hu[hu][code] = ON

    def turn_off(self, hu_input):
        hu = hu_input[0].upper()
        code = int(hu_input[1:]) - 1
        self.hu[hu][code] = OFF

STATE = State()

def get_status():
    global STATE
    return STATE.get_status()

def all_on():
    global STATE
    return STATE.all_on()

def all_off():
    global STATE
    return STATE.all_off()

def turn_on(hu):
    global STATE
    return STATE.turn_on(hu)

def turn_off(hu):
    global STATE
    return STATE.turn_off(hu)
