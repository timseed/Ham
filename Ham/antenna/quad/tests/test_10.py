from Ham.HamTest import HamTest
from Ham.antenna.quad import quad


def test_10():
    ht = HamTest()
    q = quad()

    yield HamTest(), True, q != None, "Initialized Ok"

    data = q.size(7.04)
    junk=1