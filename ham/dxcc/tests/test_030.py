from ham.HamTest import HamTest
from ham.dxcc import dxcc_all


def test_10():
    ht = HamTest()
    all_dx = dxcc_all()
    yield HamTest(), True, all_dx != None, "ham.dxcc Initialized Ok"
    all_dx.read()

    yield HamTest(), True,len(all_dx)==5504, "ham.dxcc 5504 Entries OK"

    good_country = ['A4','A71','G3','DU3','VS2','JA','HK','ZS']
    for c in good_country:
        res=all_dx.find(c)
        if res:
            yield HamTest(), True, res!=None, "Dxcc Find  OK {}".format(c)

    bad_country = ['42','968']
    for c in good_country:
        res=all_dx.find(c)
        if not res:
            yield HamTest(), True, res==None, "Dxcc Not found  OK {}".format(c)

