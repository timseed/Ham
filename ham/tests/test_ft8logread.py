from unittest import TestCase
from unittest.mock import patch, mock_open
from ham.skimmer import LoadCw,CwSpot
from datetime import datetime
from ham.mode.ft8 import LogRead

data="""200221 000030  11.0  -3  0.18 14074352 JH7OTG        QM08
        200221 000030   7.5  -4  0.08 14075982 JA6BXA        PM52
        200221 000030   8.7  -5  0.00 18101824 BH4IGO
        200221 000045  11.5  -5  0.20 14074760 JA8ECS        QN03
        200221 000100   5.7  -5  0.20  7075672 BG5GLV        PL09
        200221 000115  12.2   0  0.00  7075745 YB5HPT        OI09
        200221 000115   5.6 -12 -0.62 10137410 JP3SHI
        200221 000130   9.8   1 -0.03  7074414 XV1X          OK33
        200221 000130   3.0  -8 -0.06  7075581 DV3CEP        PK05
        200221 000145   3.3  -7 -0.02  7076183 YF5TKN        OJ20
        200221 000215  14.3  -4 -0.05  7075135 YD4URY        OI25

"""

@patch("builtins.open",mock_open(read_data=data))
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
