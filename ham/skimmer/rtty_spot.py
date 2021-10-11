from datetime import datetime
from dataclasses import dataclass


@dataclass
class RttySpot:
    # A Line looks like this
    # 0                                                                                                   1
    # 0         1         2         3         4         5         6         7         8         9         0
    # 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
    # '2021-09-24 08:14:08Z   21087.1  4D3X        24-Sep-2021 0814Z   14 dB  45 BPS  CQ RTTY       <DU3TW-#>'

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
