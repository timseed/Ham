from ham.skimmer import CwSpot 
from datetime import datetime

class LoadCw:

    def __init__(self,filename:str):

        # We want to process a Skimmer Cw Spot file
        self.lines=[]
        with open(filename,"rt") as data_in:
            for l in data_in.read().split('\n'):
                if len(l):
                    spot = CwSpot(datetime.strptime(l[0:20],'%Y-%m-%d %H:%M:%SZ'),
                               float(l[21:30]),
                               l[30:43].strip(),
                               l[44:61].strip(),
                               l[61:69].strip(),
                               l[69:77].strip(),
                               l[77:81].strip(),
                               l[81:89].strip(),
                               l[90:].strip())
                    self.lines.append(spot)
        # And we now have a list of SkimmerSpot's

    def get(self):
        return self.lines

    def len(self):
        return len(self.lines)
