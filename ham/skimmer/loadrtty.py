from ham.skimmer import RttySpot
from datetime import datetime

class LoadRtty:

    def __init__(self):
        a=1

    def fromfile(self,filename:str):

        # We want to process a Skimmer RTTY Spot file
        self.lines=[]
        with open(filename,"rt") as data_in:
            for l in data_in.read().split('\n'):
                if len(l):
                    spot = self.fromline(l)
                    self.lines.append(spot)
        # And we now have a list of SkimmerSpot's

    def get(self):
        return self.lines

    def len(self):
        return len(self.lines)

    def fromline(self,l:str):
        spot = RttySpot(datetime.strptime(l[0:20],'%Y-%m-%d %H:%M:%S%z'),
                               float(l[21:30]),
                               l[30:43].strip(),
                               l[44:61].strip(),
                               l[61:69].strip(),
                               l[69:77].strip(),
                               l[77:81].strip(),
                               l[81:89].strip(),
                               l[90:].strip())
        return spot
