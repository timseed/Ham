

class square(object):
    def __init__(self,h,w):
        self.rect=((0,0),(0,h),(h,w),(0,w))

    def get(self):
        return self.rect

class quad(object):
    speed_of_light = 299792458  #km/s

    def size(self, freq, elements=2):

        elements=[]
        wavelength=(quad.speed_of_light/1000000)/freq
        print("Freq {:5.2f} has a Wavelength {:5.2f}".format(freq, wavelength))

        #Driven Element
        driven = square(wavelength/4.0*1.05,wavelength/4.0*1.05).get()
        elements.append(driven)

        director = square(wavelength / 4.0 * 1.0, wavelength / 4.0 * 1.0).get()
        elements.append(director)

        from pprint import pprint
        pprint(elements)





