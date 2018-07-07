from math import pow


class wind_force(object):
    """
    Some general Wind Calcs for Antenna Loading
    Source:
    http://k7nv.com/notebook/topics/windload.html
    """

    def generic(self, area, wind_in_mph, drag=1.2):
        """
        A = The projected area of the item

        P , Wind pressure (Psf), = .00256 x V^2  (V= wind speed in Mph)

        Cd , Drag coefficient,  = 2.0 for flat plates. For a long cylinder (like most antenna tubes), Cd = 1.2.
        Note the relationship between them is 1.2/2 = .6, not quite 2/3.
        """
        P = 0.0256 * wind_in_mph * wind_in_mph
        F = P * area * drag
        return F

    def eia222f(self, area, wind_in_mph, drag=1.2, height_in_meters=10):
        """
        This is a newer version of the Electronic Industries Assoc. spec.

        Force = A x P x Cd x Kz x Gh
        """
        P = 0.0256 * wind_in_mph * wind_in_mph
        kz = pow((height_in_meters * 3.3 / 33), (2.0 / 7.0))
        gf = pow(.65 + .60 / (height_in_meters * 3.3 / 33), (1.0 / 7.0))
        F = P * area * drag * kz * gf
        return F


if __name__ == "__main__":
    wf = wind_force()
    ant_size = 12.5
    for wind_in_mph in range(20, 80):
        force = wf.generic(ant_size, wind_in_mph)  # TH11 Strong wind
        print(str.format("TH11 in {} mph wind has a force of {} ", wind_in_mph, force))
