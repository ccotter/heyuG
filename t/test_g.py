import unittest
import requests

class TestG(unittest.TestCase):

    def _url(self, p):
        return "http://localhost:5000/{}".format(p)

    def _get(self, p):
        r = requests.get(self._url(p))
        return r.text

    def test_home(self):
        print(self._get("/"))
