from ham.skimmer import ClusterSpot 
from datetime import datetime
# 0         1         2         3         4         5         6         7         8         9         0
# 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# HA6FQ:     14139.0  UA9CDC/M     CB37                           1032Z KN07',
# G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z IO93',
# G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z',


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
        spot = ClusterSpot(l[61:70].strip(),
                               float(l[8:18]),
                               l[19:31].strip(),
                               l[61:70].strip(),
                               "Db",
                               "Speed",
                               "Op",
                               "Mode",
                               l.split(':')[0].strip())
        return spot
