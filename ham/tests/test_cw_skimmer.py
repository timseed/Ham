from unittest import TestCase

from unittest.mock import patch, mock_open
from ham.skimmer import LoadCw,CwSpot
from datetime import datetime



data="""2021-10-08 08:38:26Z    7028.5  JE1PMQ      08-Oct-2021 0838Z   11 dB  17 WPM  CQ            <DU3TW-#>
2021-10-08 08:43:23Z   21028.8  JE1CSW      08-Oct-2021 0843Z    8 dB  24 WPM                <DU3TW-#>
2021-10-08 08:49:43Z   21027.1  JE1CSW      08-Oct-2021 0849Z    5 dB  23 WPM                <DU3TW-#>
2021-10-08 08:50:26Z   21029.4  JG3WJN      08-Oct-2021 0850Z    4 dB  31 WPM                <DU3TW-#>
2021-10-08 08:50:49Z   21028.9  JH1GZE      08-Oct-2021 0850Z    6 dB  29 WPM                <DU3TW-#>
2021-10-08 08:51:20Z   21028.1  JH0INP      08-Oct-2021 0851Z    4 dB  28 WPM                <DU3TW-#>
2021-10-08 08:55:00Z   21027.9  JA7MBT      08-Oct-2021 0855Z    4 dB  24 WPM                <DU3TW-#>
2021-10-08 08:56:00Z   21027.0  JA7MBT      08-Oct-2021 0856Z    9 dB  23 WPM                <DU3TW-#>
2021-10-08 08:56:29Z    7016.0  BD7JZC      08-Oct-2021 0856Z    9 dB  23 WPM                <DU3TW-#>
2021-10-08 08:56:30Z    7016.0  BD7JZC      08-Oct-2021 0856Z    9 dB  23 WPM  CQ            <DU3TW-#>
2021-10-08 08:58:25Z   21030.8  JA1BOQ      08-Oct-2021 0858Z    5 dB  33 WPM                <DU3TW-#>
2021-10-08 08:58:44Z   21026.7  JF1EHM      08-Oct-2021 0858Z    4 dB  28 WPM                <DU3TW-#>
2021-10-08 09:00:09Z   21027.7  JF1RYU      08-Oct-2021 0900Z    2 dB  27 WPM                <DU3TW-#>
2021-10-08 09:01:59Z   21028.4  JP1FHC      08-Oct-2021 0901Z    7 dB  27 WPM                <DU3TW-#>
2021-10-08 09:02:51Z   21027.9  JM1SZY      08-Oct-2021 0902Z    4 dB  26 WPM                <DU3TW-#>
2021-10-08 09:07:22Z    7002.0  JM7OLW      08-Oct-2021 0907Z    6 dB  28 WPM  CQ            <DU3TW-#>
2021-10-08 09:12:09Z    7020.0  JM8IO       08-Oct-2021 0912Z    6 dB  21 WPM                <DU3TW-#>
2021-10-08 09:12:30Z    7006.5  JH7WFF      08-Oct-2021 0912Z    5 dB  24 WPM                <DU3TW-#>
2021-10-08 09:12:51Z    7006.5  JA6CQ       08-Oct-2021 0912Z    6 dB  22 WPM                <DU3TW-#>
2021-10-08 09:20:53Z   21026.8  JH1ECG      08-Oct-2021 0920Z    4 dB  29 WPM                <DU3TW-#>
2021-10-08 09:25:53Z    7011.0  JF3KCH      08-Oct-2021 0925Z    8 dB  10 WPM  DE            <DU3TW-#>
2021-10-08 09:26:42Z    7023.0  BH4FCD      08-Oct-2021 0926Z    5 dB  22 WPM  CQ            <DU3TW-#>
2021-10-08 09:30:16Z    7021.4  8H20PON     08-Oct-2021 0930Z    6 dB  18 WPM  DE            <DU3TW-#>
2021-10-08 09:30:18Z    7014.0  8J9YAF/P    08-Oct-2021 0930Z    9 dB  29 WPM  CQ            <DU3TW-#>
2021-10-08 09:32:00Z    7011.0  JR8TIR      08-Oct-2021 0932Z   16 dB  19 WPM                <DU3TW-#>
2021-10-08 09:35:55Z    7013.1  JG0AW       08-Oct-2021 0935Z    5 dB  23 WPM                <DU3TW-#>
2021-10-08 09:39:09Z    7013.0  JE1AZZ      08-Oct-2021 0939Z    8 dB  18 WPM  DE            <DU3TW-#>"""



class TestCwSkimmer(TestCase):
    def setUp(self) -> None:
        """
        This runs before every test
        :return:
        """
        a=1
        
        

        

      
    @patch("builtins.open",mock_open(read_data=data))
    def test_read(self):
        spots=LoadCw("fake_file")
        self.assertEqual(spots.len(),27)
        china_station= spots.get()[8]   
        self.assertIsInstance(china_station,CwSpot)
        self.assertEqual(china_station.call,"BD7JZC")
        self.assertEqual(china_station.freq,7016.0)
        self.assertEqual(china_station.stength,"9 dB")
        self.assertEqual(china_station.speed,"23 WPM")
