
class HamTest(object):

    def __call__(self, expected_result, value, test_name):
        assert expected_result == value, "HamTest: {}".format(test_name)

