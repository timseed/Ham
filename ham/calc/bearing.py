import geopy
from ham.dxcc import dxcc_all
from haversine import haversine

class bearing(object):
    
    def __init__(self, homecountry='A4'):
        self.dx_list = dxcc_all()
        self.dx_list.read()
        self.home=None
        #self.dx_list.showall()
        try:
            self.home=self.dx_list.find(homecountry)
        except Exception as err:
            print("Error finding home_country" + str(err))

    def distance_to_kms(self, country):
        dx=self.dx_list.show(country)
        if dx is not None and self.home is not None:
            # given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
            country_bearing = haversine((self.home.Latitude(),
                                         self.home.Longitude()),
                                        (dx.Latitude(),dx.Longitude()),miles = False)
            return country_bearing
        else:
            return None

    def check(self):
        '''
        Check to see is Prefix A is found.
        Written when I was living in A4


        :return:  True/False not the greatest test !!
        '''
        b=self.dx_list.prefix()
        for c in b:
            if c.startswith('A'):
                print(''+c)
                return True
        return False

if __name__=="__main__":
    b=bearing('A4')
    b.check()
    for ctry in ['A9','G','DU','JA','K']:
        beam=b.distance_to_kms(ctry)
        print(str.format("From A4 to {} is {}",ctry,beam))
