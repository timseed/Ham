from unittest import TestCase
from ham.dxcc import SCP
from pprint import pprint


class TestScp(TestCase):

    def setUp(self) -> None:
        """
        This runs before every test
        :return:
        """
        self.myscp = SCP()

    def test_instance(self):
        self.assertTrue(type(self.myscp) is SCP)

    def test_count(self):
        self.assertGreater(self.myscp.count,500)

    def test_data(self):
        d=self.myscp.Data
        self.assertTrue(type(d) is list)
        self.assertTrue(len(d)==self.myscp.count)

    def test_I_am_in(self):
        self.assertTrue('DU3TW' in self.myscp.Data)

    def test_my_uk_not_in(self):
        self.assertTrue('M0FGC' not in self.myscp.Data)

    def test_line_ten(self):
        self.assertNotEqual("junk",self.myscp.Data[9])
