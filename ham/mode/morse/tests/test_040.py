from ham.HamTest import HamTest
from ham.mode import morse


def test_40():
    cw = morse()

    yield HamTest(), True, cw !=None, "Morse Initialized OK"