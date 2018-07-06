from Ham.HamTest import HamTest
from Ham.mode import morse


def test_40():
    cw = morse()

    yield HamTest(), True, cw !=None, "Morse Initialized OK"