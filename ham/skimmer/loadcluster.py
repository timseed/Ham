from ham.skimmer import ClusterSpot 
from datetime import datetime
# 0         1         2         3         4         5         6         7         8         9         0
# 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# HA6FQ:     14139.0  UA9CDC/M     CB37                           1032Z KN07',
# G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z IO93',
# G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z',

# OH6BG-#:    3520.9  SM4CUQ       CW 39 dB 19 WPM CQ             0812Z
# VE6WZ-#:   14100.0  W6WX         CW 12 dB 22 WPM NCDXF BCN      0812Z
# IK4VET-#:  14028.0  9A9BB        CW  7 dB 25 WPM CQ             0812Z
# BG4GOV-#:  21025.1  YC0RNC/1     CW 12 dB 18 WPM CQ             0812Z
# VK4CT-#:   14058.0  F/HB9CBR/P   CW 11 dB 24 WPM CQ             0812Z
# R9IR-#:    21020.0  UT2IY        CW  4 dB 26 WPM CQ             0812Z

class LoadCluster:

    def __init__(self):
        a=1

    def fromfile(self,filename:str):
        # We want to process a Dx Cluster Spot file
        self.spots=[]
        with open(filename,"rt") as data_in:
            for l in data_in.read().split('\n'):
                if len(l):
                    spot = self.fromline(l)
                    self.spots.append(spot)
        # And we now have a list of SkimmerSpot's

    def empty(self):
        self.spots=[]

    def get(self):
        return self.spots

    def len(self):
        return len(self.spots)

    def fromline(self,l:str):

        if (l[33:35].upper()=='CW'):
            spot = ClusterSpot(l[61:70].strip(),
                               float(l[11:18]),
                               l[19:31].strip(),
                               l[61:70].strip(),
                               l[36:38].strip(),
                               l[42:44],
                               l[49:51],
                               l[33:35].upper(),
                               l.split(':')[0].strip())
        else:
            spot = ClusterSpot(l[61:70].strip(),
                               float(l[11:18]),
                               l[19:31].strip(),
                               l[61:70].strip(),
                               "Db",
                               "Speed",
                               "Op",
                               "Mode",
                               l.split(':')[0].strip())
        return spot
