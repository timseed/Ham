from unittest import TestCase

from ham.dxcc.dxobj import DxObj


class TestDxObj(TestCase):

    def setUp(self) -> None:
        self.dx = DxObj(call_starts="OS",
                        country_name="Outer Space",
                        cq_zone=99,
                        itu_zone=101,
                        continent_abbreviation='OS',
                        latitude=15.0,
                        longitude=120.0,
                        local_time_offset=8.0, )
        self.expected="Country:'Outer Space',CQ:99,ITU:101,Continent_Abbreviation:'OS',Latitude:15.0,Longitude:120.0,Local_time_offset:8.0"


    def test_instance(self):
        self.assertIsInstance(self.dx, DxObj)

    def test_values(self):
        self.assertEqual(self.dx.Country_Name,"Outer Space")
        self.assertEqual(self.dx.CQ_Zone,99)
        self.assertEqual(self.dx.ITU_Zone,101)
        self.assertEqual(self.dx.Continent_Abbreviation,'OS')
        self.assertEqual(self.dx.Latitude,15.0)
        self.assertEqual(self.dx.Longitude,120.0)
        self.assertEqual(self.dx.Local_time_offset,8.0)

    def test_dump(self):
        self.assertEqual(self.dx.dump(),self.expected)

    def test_show(self):
        self.assertEqual(self.dx.show(), None)

    def test_str(self):
        self.assertEqual(str(self.dx),self.expected)