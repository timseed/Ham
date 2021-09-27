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
    stength: str
    speed: str
    op: str
    mode: str
    spotter: str
