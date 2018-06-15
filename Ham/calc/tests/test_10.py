from Ham.HamTest import HamTest
from Ham.calc import bearing
from Ham.calc import locator


def test_10():
    ht = HamTest()
    b = bearing()

    yield HamTest(), True, b != None, "ham.calc.bearing Initialized Ok"

    b = bearing('A4')
    good_test = [('A9', 853.1458012135847),
                 ('G ', 5941.158849483864),
                 ('DU', 6751.18918722129),
                 ('JA', 7607.903353972733),
                 ('K ', 12538.21722484994),
                 ]

    bad_test = [('92', 853.1458012135847),
                ('44', 853.1458012135847),
                ]

    # These are known Countries
    for t in good_test:
        beam = b.distance_to_kms(t[0])
        yield HamTest(), True, beam != None, "ham.calc.bearing Country Found {}".format(t[1])
        yield HamTest(), True, beam == t[1], "ham.calc.bearing Distance Ok {}->{}".format(t[1], beam)

        # These are known Countries
    for t in bad_test:
        beam = b.distance_to_kms(t[0])
        yield HamTest(), True, beam is None, "ham.calc.bearing Country Not Found {}".format(t[0])


def test_20():
    ht = HamTest()

    l = locator()
    yield HamTest(), True, l != None, "ham.calc.locator Initialized Ok"
    mct_grid = l.latlong_to_locator(23.3, 58.3)

    pos = l.locator_to_latlong(mct_grid)

    pos = l.locator_to_latlong(mct_grid)
    yield HamTest(), True , mct_grid == "LL93DH", "Muscat Grid Calculated ok"
    # Get Telepayong grid
    tele_grid = l.latlong_to_locator(15.19, 120.78)
    dist = l.calculate_distance(mct_grid, tele_grid)

    short_path_bearing = l.calculate_heading(mct_grid, tele_grid)
    long_path_bearing = l.calculate_heading_longpath(mct_grid, tele_grid)
    yield HamTest(), True, tele_grid == "PK05JE", "Pampanga QTH Grid Calculated ok"
    yield HamTest(), True, dist == 6576.247536801719, "Distance in kms"
    yield HamTest(), True, short_path_bearing == float(85.70847922042742),"Muscat to Pampanga Short Path"
    yield HamTest(), True, long_path_bearing == float(265.7084792204274), "Muscat to Pampanga Long Path"
