from unittest import TestCase

from unittest.mock import patch, mock_open
from ham.skimmer import LoadCluster, ClusterSpot
from datetime import datetime


data = """SP5MXG:    21074.0  MI0JZZ       FT8 +02dB from IO65 2559Hz     1031Z
 SP5MXG:    21074.0  MI0JZZ       FT8 +02dB from IO65 2559Hz     1031Z
 HA6FQ:     14139.0  UA9CDC/M     CB37                           1032Z
 HA6FQ:     14139.0  UA9CDC/M     CB37                           1032Z KN07
 G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z IO93
 G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z
 ON8ON:     18133.0  VK2BY        Brad CQn 55-57/Hexbeam         1032Z
 ON8ON:     18133.0  VK2BY        Brad CQn 55-57/Hexbeam         1032Z
 BA5CW:     24915.0  9V1ZV        FT8 -14dB from OJ11 2585Hz     1033Z
 BA5CW:     24915.0  9V1ZV        FT8 -14dB from OJ11 2585Hz     1033Z PM01'"""

expected_dict = {
    "call": "MI0JZZ",
    "freq": 21074.0,
    "mode": "Mode",
    "op": "Op",
    "speed": "Speed",
    "spotter": "SP5MXG",
    "stength": "Db",
    "when_full": "1031Z",
    "when_no_sec": "1031Z",
}


class TestCluster(TestCase):
    def setUp(self) -> None:
        """
        This runs before every test
        :return:
        """
        a = 1

    @patch("builtins.open", mock_open(read_data=data))
    def test_read(self):
        spots = LoadCluster()
        spots.fromfile("fake")
        self.assertEqual(spots.len(), 10)
        ni_station = spots.get()[1]
        self.assertIsInstance(ni_station, ClusterSpot)
        self.assertEqual(ni_station.call, "MI0JZZ")
        self.assertEqual(ni_station.freq, 21074.0)
        self.assertEqual(ni_station.spotter, "SP5MXG")
        self.assertEqual(ni_station.to_dict(), expected_dict)


    @patch("builtins.open", mock_open(read_data=data))
    def test_line(self):
        spots = LoadCluster()
        spots.fromfile("fake")
        ni_station = spots.fromline("SP5MXG:    21074.0  MI0JZZ       FT8 +02dB from IO65 2559Hz     1031Z")
        self.assertIsInstance(ni_station, ClusterSpot)
        self.assertEqual(ni_station.call, "MI0JZZ")
        self.assertEqual(ni_station.freq, 21074.0)
        self.assertEqual(ni_station.spotter, "SP5MXG")
        self.assertEqual(ni_station.to_dict(), expected_dict)