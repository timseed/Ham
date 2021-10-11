from datetime import datetime
from dataclasses import dataclass


@dataclass
class CwSpot:
    # A Line looks like this
    # 0                                                                                                   1
    # 0         1         2         3         4         5         6         7         8         9         0
    # 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
    #  2021-10-08 09:07:22Z    7002.0  JM7OLW      08-Oct-2021 0907Z    6 dB  28 WPM  CQ            <DU3TW-#>
    #  2021-10-08 09:12:09Z    7020.0  JM8IO       08-Oct-2021 0912Z    6 dB  21 WPM                <DU3TW-#>

    """Class for keeping track of an spot."""
    when_full: datetime
    freq: float
    call: str
    when_no_sec: str
    strength: str
    speed: str
    op: str
    mode: str
    spotter: str


    def to_dict(self):
        return {
            'when_full': self.when_full,
            'freq': self.freq, 
            'call': self.call,
            'when_no_sec': self.when_no_sec,
            'strength': self.stength,
            'speed': self.speed,
            'op': self.op,
            'mode': self.mode,
            'spotter': self.spotter
        }
