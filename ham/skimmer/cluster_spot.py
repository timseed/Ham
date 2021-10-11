from time import time
from dataclasses import dataclass


@dataclass
class ClusterSpot:
    # A Line looks like this
    # 0                                                                                                   1
    # 0         1         2         3         4         5         6         7         8         9         0
    # 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
    # HA6FQ:     14139.0  UA9CDC/M     CB37                           1032Z KN07',
    # G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z IO93',
    # G1XOW:     21207.0  PX8I         cq cq cq 55                    1032Z',
    # ON8ON:     18133.0  VK2BY        Brad CQn 55-57/Hexbeam         1032Z',
    """Class for keeping track of an spot."""
    when_full: time
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
