from unittest import TestCase
from ham.calc import Locator
from ham.i2 import i2_country_name


class TestDxccAll(TestCase):
    def setUp(self):
        self.i2c = i2_country_name()

    def test_01_no_change(self):
        """These countrie should not need changing"""
        cty = ["England", "France", "Saudi		Arabia"]
        for c in cty:
            self.assertEqual(self.i2c.i2Name(c), c)

    def test_02_change(self):
        """These		countries do need		changing"""
        t = {
            "East Malaysia": "Malaysia",
            "West Malaysia": "Malaysia",
            "Hawaii": "USA",
            "European Russia": "Russia",
            "Asiatic Russia": "Russia",
            "Asiatic Turkey": "Russia",
            "Andaman & Nicobar Is.": "India",
            "Ascension Island": "UK",
            "European Turkey": "Turkey",
        }
        for k, v in t.items():
            self.assertEqual(self.i2c.i2Name(k), v)
