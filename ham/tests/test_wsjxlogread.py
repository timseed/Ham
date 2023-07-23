from unittest import TestCase

from unittest.mock import patch, mock_open
from ham.skimmer import LoadCw,CwSpot
from datetime import datetime

from ham.mode.wsjx import LogRead



data="""<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:18:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JA1MNM <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:24:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>VK6KBY <grid:6>OF76LM <grid:19>-33.479166666666664 <grid:18>114.95833333333334 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:36:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JA1MNM <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:36:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>VK6KBY <grid:6>OF76LM <grid:19>-33.479166666666664 <grid:18>114.95833333333334 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:54:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JA1MNM <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 02:56:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>VK6KBY <grid:6>OF76LM <grid:19>-33.479166666666664 <grid:18>114.95833333333334 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:04:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>VK6KBY <grid:6>OF76LM <grid:19>-33.479166666666664 <grid:18>114.95833333333334 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:16:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JA1MNM <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:22:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>VK6KBY <grid:6>OF76LM <grid:19>-33.479166666666664 <grid:18>114.95833333333334 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:26:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JI1BQW <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:30:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JH3KTL <grid:6>PM74LM <grid:18>34.520833333333336 <grid:18>134.95833333333331 <EOR>
<freq:2>20 <mode:3>FT8 <date:25>2019-04-21 03:34:00+00:00 <timeofday:3>unk <my_call:5>DU3TW <their_call:6>JA1MNM <grid:6>PM95LM <grid:18>35.520833333333336 <grid:18>138.95833333333331 <EOR>"""

class test_ft8LogRead(TestCase):
    def setUp(self) -> None:
        self.mode = LogRead()

    def test_is_object(self):
        self.assertIsInstance(self.mode, LogRead)

    def test_process(self):
        assert True

    def test_dump(self):
        assert True

    def test_dump_geo(self):
        assert True

    def test_dump_geo_to_file(self):
        assert True
