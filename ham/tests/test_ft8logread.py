




from unittest import TestCase
from unittest.mock import patch, mock_open
from datetime import datetime
from ham.mode.ft8 import LogRead
from pprint import pprint

data="""200221 000030  11.0  -3  0.18 14074352 JH7OTG        QM08
"""

class test_ft8LogRead(TestCase):

    @patch("builtins.open", mock_open(read_data=data))
    def setUp(self) -> None:
        self.mode = LogRead()
        

    def test_is_object(self):
        self.assertIsInstance(self.mode, LogRead)

    @patch("builtins.open", mock_open(read_data=data))
    def test_records(self):
        self.assertEqual(1,self.mode.len())

    @patch("builtins.open", mock_open(read_data=data))
    def test_fake_load(self):
        self.assertEqual(self.mode.load_file(),data.split('\n'))
        pprint(self.mode.dump())
        self.assertEqual(1,self.mode.len())

        

    def test_process(self):
        assert True

    def test_dump(self):
        pprint(self.mode.dump_data())
        self.assertEqual([{'band': 20,
  'bearing': 33.42693350402328,
  'call': 'JH7OTG',
  'distance': 3259.8701510830274,
  'my_lat': 15.1875,
  'my_lon': 120.79166666666667,
  'their_lat': 38.520833333333336,
  'their_lon': 140.95833333333331,
  'when': 0}], self.mode.dump_data())

    def test_dump_geo(self):
        assert True

    def test_dump_geo_to_file(self):
        assert True

