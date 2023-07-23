class FrequencyMode(object):
    """
	Guess Mode from the Frequency
    """

    def __init__(self, contest=True):
        self.contest = contest
        self.bm_contest = {'FT8': [(14072.0, 14075.0),
                                   (21072.0, 21075.0),
                                   (28072.0, 28075.0)],
                           'CW': [(1810.0, 1840.0),
                                  (3500.0, 3570.0),
                                  (7000.0, 7060.0),
                                  (14000.0, 14065.0),
                                  (21000.0, 21065.0),
                                  (28000.0, 28065.0)],
                           'SSB': [(3650.0, 3850.0),
                                   (7060.0, 7200.0),
                                   (14120.0, 14400.0),
                                   (21120, 21400.0),
                                   (28350, 28600.0)],
                           'RTTY': [(14065, 14099.0),
                                    (14101.0, 14120.0),
                                    (21065.0, 21099.0),
                                    (21101.0, 21120.0),
                                    (28065.0, 28120.0),
                                    (28101.0, 28120.0)]}

        self.bm_no_contest = {'FT8': [(10130.0, 10150.0),
                                      (14072.0, 14075.0),
                                      (18095.0, 18105.0),
                                      (21072.0, 21075.0),
                                      (24915.0, 24920.0),
                                      (28072.0, 28075.0)],
                              'CW': [(1810, 1840),
                                     (3500.0, 3570.0),
                                     (7000.0, 7040.0),
                                     (10100.0, 10130.0),
                                     (14000.0, 14060.0),
                                     (18068.0, 18095.0),
                                     (21000.0, 21065.0),
                                     (24890.0, 24915.0),
                                     (28000.0, 28065.0)],
                              'SSB': [(3650.0, 3850.0),
                                      (7060.0, 7200.0),
                                      (14120.0, 14400.0),
                                      (18120.0, 18168.0),
                                      (21120.0, 21400.0),
                                      (24940.0, 24990.0),
                                      (28350.0, 28600.0)],
                              'RTTY': [(14065.0, 14099.0),
                                       (21065.0, 21099.0),
                                       (24915.0, 24925.0),
                                       (28065.0, 28120.0)
                                       ]}

    def Mode(self, freqfnfhz: float) -> str:
        """
           Estimate what Mode the signal should be in
        """
        if self.contest:
            check_data = self.bm_contest
        else:
            check_data = self.bm_no_contest

        # need to check FT8 first
        for freq_range in check_data['FT8']:
            if freqfnfhz > freq_range[0] and freqfnfhz < freq_range[1]:
                return 'FT8'
        else:
            for k in check_data.keys():
                for freq_range in check_data[k]:
                    if freqfnfhz > freq_range[0] and freqfnfhz < freq_range[1]:
                        return k
        return "Unk"
