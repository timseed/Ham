class i2_country_name(object):
    """
    Some of the Country names from DXCC are not valid in i2.

    A lot of the DXCC Entities are islands ... which are not common for me - so I have
    not added them here at the moment.
    """


    def __init__(self):
        self.change={
        'Canary Islands':'Spain',
        'East Malaysia':'Malaysia',
        'West Malaysia':'Malaysia',
        'Hawaii':'USA',
        'European Russia':'Russia',
        'Asiatic Russia':'Russia',
        'Asiatic Turkey':'Russia',
        'Andaman & Nicobar Is.':'India',
        'Ascension Island':'UK',
        'European Turkey':'Turkey',
        }


    def i2Name(self, ctry:str)->str:
        if ctry in self.change:
            return self.change[ctry]
        else:
            return ctry
