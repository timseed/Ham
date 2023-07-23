from unittest import TestCase
from ham.cw import Cw
from pprint import pprint


class Testcw(TestCase):
    def setUp(self) -> None:
        """
        This runs before every test
        :return:
        """
        self.mycw = Cw()
        self.Hi_Str="HI 1"
        self.Cq_Str="CQ CQ de"

    def test_instance(self):
        self.assertTrue(type(self.mycw) is Cw)

    def test_char_A(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("A") == ".-")

    def test_char_B(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("B") == "-...")

    def test_char_C(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("C") == "-.-.")

    def test_char_D(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("D") == "-..")

    def test_char_E(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("E") == ".")

    def test_char_F(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("F") == "..-.")

    def test_char_G(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("G") == "--.")

    def test_char_H(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("H") == "....")

    def test_char_I(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("I") == "..")

    def test_char_J(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("J") == ".---")

    def test_char_K(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("K") == "-.-")

    def test_char_L(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("L") == ".-..")

    def test_char_M(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("M") == "--")

    def test_char_N(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("N") == "-.")

    def test_char_O(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("O") == "---")

    def test_char_P(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("P") == ".--.")

    def test_char_Q(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("Q") == "--.-")

    def test_char_R(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("R") == ".-.")

    def test_char_S(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("S") == "...")

    def test_char_T(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("T") == "-")

    def test_char_U(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("U") == "..-")

    def test_char_V(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("V") == "...-")

    def test_char_W(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("W") == ".--")

    def test_char_X(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("X") == "-..-")

    def test_char_Y(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("Y") == "-.--")

    def test_char_Z(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("Z") == "--..")

    def test_char_1(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("1") == ".----")

    def test_char_2(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("2") == "..---")

    def test_char_3(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("3") == "...--")

    def test_char_4(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("4") == "....-")

    def test_char_5(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("5") == ".....")

    def test_char_6(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("6") == "-....")

    def test_char_7(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("7") == "--...")

    def test_char_8(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("8") == "---..")

    def test_char_9(self):
        self.assertTrue(self.mycw.letter_to_dot_dash("9") == "----.")
        
    def test_len_h(self):
        # See the length in .'s
        self.assertTrue(self.mycw.len_chr("H") == 4)
        self.assertTrue(self.mycw.len_chr("h") == 4)
        self.assertTrue(self.mycw.len_chr("0") == 15)
        

    def test_cw_timing(self):
        # Now check the genreation of text to CW
        self.assertEqual(self.mycw.cw_timing(self.Hi_Str),".g.g.g.e.g.e_e.g-g-g-g-_")
        self.assertEqual(self.mycw.cw_timing(self.Cq_Str),"-g.g-g.e-g-g.g-e_e-g.g-g.e-g-g.g-e_e-g.g.e._")
       
    def test_cw_length_in_dits(self):
    
        # Using the internal representation .g.g.e 
        # How long is this in dits 
        
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Hi_Str)),50)
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Cq_Str)),98)
        
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Hi_Str.upper())),50)
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Cq_Str.upper())),98)
        
        
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Hi_Str.lower())),50)
        self.assertEqual(self.mycw.length_in_dits(self.mycw.cw_timing(self.Cq_Str.lower())),98)
        