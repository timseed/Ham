from unittest import TestCase
from ham.band import FrequencyMode


class TestFrequencyMode(TestCase):
    def setUp(self) -> None:
        """
        This runs before every test
        :return:
        """

        self.fm= FrequencyMode(contest=True)

    def test_20m(self):
        """
        Basic 20m Frequencies 
        :return:
        """

        self.assertEqual(self.fm.Mode(14021.0), "CW")
        self.assertEqual(self.fm.Mode(14043.0), "CW")
        self.assertEqual(self.fm.Mode(14221.0), "SSB")

        self.assertEqual(self.fm.Mode(14082.1), "RTTY")

        self.assertEqual(self.fm.Mode(14074.1),"FT8")


    def test_10m(self):
        """
                Basic 20m Frequencies
                :return:
                """

        self.assertEqual(self.fm.Mode(28021.0), "CW")
        self.assertEqual(self.fm.Mode(28043.0), "CW")
        self.assertEqual(self.fm.Mode(28431.0), "SSB")

        self.assertEqual(self.fm.Mode(28082.1), "RTTY")

        self.assertEqual(self.fm.Mode(28074.1), "FT8")