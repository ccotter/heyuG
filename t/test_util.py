import unittest

import heyuG.util

class TestUtil(unittest.TestCase):

    def test_parse_status_all_off(self):

        sample = """
Last addressed device =       0x0000000000000000
Status of monitored devices = 0x0000000000000000
Status of dimmed devices =    0x0000000000000000
"""

        devices = heyuG.util.parse_status_text(sample)
        expected = {i: False for i in range(1, 17)}
        self.assertEqual(expected, devices)

    def test_parse_status_all_on(self):

        sample = """
Last addressed device =       0x0000000000000000
Status of monitored devices = 0x1111111111111111
Status of dimmed devices =    0x0000000000000000
"""

        devices = heyuG.util.parse_status_text(sample)
        expected = {i: True for i in range(1, 17)}
        self.assertEqual(expected, devices)

    def test_parse_status_some_on(self):

        sample = """
Last addressed device =       0x0000000000000000
Status of monitored devices = 0x0000110010000001
Status of dimmed devices =    0x0000000000000000
"""

        devices = heyuG.util.parse_status_text(sample)
        expected = {i: False for i in range(1, 17)}
        expected[1] = True
        expected[8] = True
        expected[11] = True
        expected[12] = True
        self.assertEqual(expected, devices)

    def test_parse_status_failure(self):

        with self.assertRaises(Exception):
            heyuG.util.parse_status_text("Nothing here")

        with self.assertRaises(Exception):
            heyuG.util.parse_status_text("")
