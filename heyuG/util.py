import re

def parse_status_text(txt):
    """ Returns a dict representing the state of a given house code
    from the `heyu status` output. """

    search = re.compile("Status of monitored devices.*\((................)\)")

    devices = None
    for l in txt.splitlines():
        g = search.match(l)
        if g is not None:
            devices = g.group(1)

    if devices is None:
        raise Exception("Could not find 'monitored devices' in text")

    output = {}
    for i in range(0, 16):
        output[16-i] = devices[i] != "0"

    return output
