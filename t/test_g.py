import unittest
import requests

class TestG(unittest.TestCase):

    def _url(self, p):
        return "http://localhost:5000{}".format(p)

    def _get(self, p):
        r = requests.get(self._url(p))
        return r.text

    def _post(self, p, data):
        r = requests.post(self._url(p), data)
        return r.text



    def test_home(self):
        print(self._get("/"))

    def test_get_status(self):
        print(self._get("/heyu/status"))

    def test_all_on(self):
        print(self._post("/heyu/commands/all_on", {}))

    def test_all_off(self):
        print(self._post("/heyu/commands/all_off", {}))

    def test_a6_on(self):
        print(self._post("/heyu/commands/a6_on", {}))

    def test_a6_off(self):
        print(self._post("/heyu/commands/a6_off", {}))
