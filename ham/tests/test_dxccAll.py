from unittest import TestCase
from ham.dxcc import DxccAll


class TestDxccAll(TestCase):

    Country_List = ['Afghanistan',
 'African Italy',
 'Agalega & St. Brandon',
 'Aland Islands',
 'Alaska',
 'Albania',
 'Algeria',
 'American Samoa',
 'Amsterdam & St. Paul Is.',
 'Andaman & Nicobar Is.',
 'Andorra',
 'Angola',
 'Anguilla',
 'Annobon Island',
 'Antigua & Barbuda',
 'Argentina',
 'Armenia',
 'Aruba',
 'Ascension Island',
 'Asiatic Russia',
 'Asiatic Turkey',
 'Austral Islands',
 'Australia',
 'Austria',
 'Aves Island',
 'Azerbaijan',
 'Azores',
 'Bahamas',
 'Bahrain',
 'Baker & Howland Islands',
 'Balearic Islands',
 'Banaba Island',
 'Bangladesh',
 'Barbados',
 'Bear Island',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bermuda',
 'Bhutan',
 'Bolivia',
 'Bonaire',
 'Bosnia-Herzegovina',
 'Botswana',
 'Bouvet',
 'Brazil',
 'British Virgin Islands',
 'Brunei Darussalam',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Canary Islands',
 'Cape Verde',
 'Cayman Islands',
 'Central African Republic',
 'Central Kiribati',
 'Ceuta & Melilla',
 'Chad',
 'Chagos Islands',
 'Chatham Islands',
 'Chesterfield Islands',
 'Chile',
 'China',
 'Christmas Island',
 'Clipperton Island',
 'Cocos (Keeling) Islands',
 'Cocos Island',
 'Colombia',
 'Comoros',
 'Conway Reef',
 'Corsica',
 'Costa Rica',
 "Cote d'Ivoire",
 'Crete',
 'Croatia',
 'Crozet Island',
 'Cuba',
 'Curacao',
 'Cyprus',
 'Czech Republic',
 'DPR of Korea',
 'Dem. Rep. of the Congo',
 'Denmark',
 'Desecheo Island',
 'Djibouti',
 'Dodecanese',
 'Dominica',
 'Dominican Republic',
 'Ducie Island',
 'East Malaysia',
 'Easter Island',
 'Eastern Kiribati',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'England',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Ethiopia',
 'European Russia',
 'European Turkey',
 'Falkland Islands',
 'Faroe Islands',
 'Fed. Rep. of Germany',
 'Fernando de Noronha',
 'Fiji',
 'Finland',
 'France',
 'Franz Josef Land',
 'French Guiana',
 'French Polynesia',
 'Gabon',
 'Galapagos Islands',
 'Georgia',
 'Ghana',
 'Gibraltar',
 'Glorioso Islands',
 'Greece',
 'Greenland',
 'Grenada',
 'Guadeloupe',
 'Guam',
 'Guantanamo Bay',
 'Guatemala',
 'Guernsey',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Hawaii',
 'Heard Island',
 'Honduras',
 'Hong Kong',
 'Hungary',
 'ITU HQ',
 'Iceland',
 'India',
 'Indonesia',
 'Iran',
 'Iraq',
 'Ireland',
 'Isle of Man',
 'Israel',
 'Italy',
 'Jamaica',
 'Jan Mayen',
 'Japan',
 'Jersey',
 'Johnston Island',
 'Jordan',
 'Juan Fernandez Islands',
 'Juan de Nova, Europa',
 'Kaliningrad',
 'Kazakhstan',
 'Kenya',
 'Kerguelen Islands',
 'Kermadec Islands',
 'Kingman Reef',
 'Kosovo',
 'Kure Island',
 'Kuwait',
 'Kyrgyzstan',
 'Lakshadweep Islands',
 'Laos',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Liechtenstein',
 'Lithuania',
 'Lord Howe Island',
 'Luxembourg',
 'Macao',
 'Macedonia',
 'Macquarie Island',
 'Madagascar',
 'Madeira Islands',
 'Malawi',
 'Maldives',
 'Mali',
 'Malpelo Island',
 'Malta',
 'Mariana Islands',
 'Market Reef',
 'Marquesas Islands',
 'Marshall Islands',
 'Martinique',
 'Mauritania',
 'Mauritius',
 'Mayotte',
 'Mellish Reef',
 'Mexico',
 'Micronesia',
 'Midway Island',
 'Minami Torishima',
 'Moldova',
 'Monaco',
 'Mongolia',
 'Montenegro',
 'Montserrat',
 'Morocco',
 'Mount Athos',
 'Mozambique',
 'Myanmar',
 'N.Z. Subantarctic Is.',
 'Namibia',
 'Nauru',
 'Navassa Island',
 'Nepal',
 'Netherlands',
 'New Caledonia',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'Niue',
 'Norfolk Island',
 'North Cook Islands',
 'Northern Ireland',
 'Norway',
 'Ogasawara',
 'Oman',
 'Pakistan',
 'Palau',
 'Palestine',
 'Palmyra & Jarvis Islands',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Peter 1 Island',
 'Philippines',
 'Pitcairn Island',
 'Poland',
 'Portugal',
 'Pr. Edward & Marion Is.',
 'Pratas Island',
 'Puerto Rico',
 'Qatar',
 'Republic of Korea',
 'Republic of South Sudan',
 'Republic of the Congo',
 'Reunion Island',
 'Revillagigedo',
 'Rodriguez Island',
 'Romania',
 'Rotuma Island',
 'Rwanda',
 'Saba & St. Eustatius',
 'Sable Island',
 'Samoa',
 'San Andres & Providencia',
 'San Felix & San Ambrosio',
 'San Marino',
 'Sao Tome & Principe',
 'Sardinia',
 'Saudi Arabia',
 'Scarborough Reef',
 'Scotland',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Shetland Islands',
 'Sicily',
 'Sierra Leone',
 'Singapore',
 'Sint Maarten',
 'Slovak Republic',
 'Slovenia',
 'Solomon Islands',
 'Somalia',
 'South Africa',
 'South Cook Islands',
 'South Georgia Island',
 'South Orkney Islands',
 'South Sandwich Islands',
 'South Shetland Islands',
 'Sov Mil Order of Malta',
 'Spain',
 'Spratly Islands',
 'Sri Lanka',
 'St. Barthelemy',
 'St. Helena',
 'St. Kitts & Nevis',
 'St. Lucia',
 'St. Martin',
 'St. Paul Island',
 'St. Peter & St. Paul',
 'St. Pierre & Miquelon',
 'St. Vincent',
 'Sudan',
 'Suriname',
 'Svalbard',
 'Swains Island',
 'Swaziland',
 'Sweden',
 'Switzerland',
 'Syria',
 'Taiwan',
 'Tajikistan',
 'Tanzania',
 'Temotu Province',
 'Thailand',
 'The Gambia',
 'Timor - Leste',
 'Togo',
 'Tokelau Islands',
 'Tonga',
 'Trindade & Martim Vaz',
 'Trinidad & Tobago',
 'Tristan da Cunha & Gough',
 'Tromelin Island',
 'Tunisia',
 'Turkmenistan',
 'Turks & Caicos Islands',
 'Tuvalu',
 'UK Base Areas on Cyprus',
 'US Virgin Islands',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Nations HQ',
 'United States',
 'Uruguay',
 'Uzbekistan',
 'Vanuatu',
 'Vatican City',
 'Venezuela',
 'Vietnam',
 'Wake Island',
 'Wales',
 'Wallis & Futuna Islands',
 'West Malaysia',
 'Western Kiribati',
 'Western Sahara',
 'Willis Island',
 'Yemen',
 'Zambia',
 'Zimbabwe']


    def setUp(self) -> None:
        self.dxcc_all = DxccAll()

    def test_init_ok(self):
        self.assertTrue(self.dxcc_all)

    def test_removewae(self):
        self.assertTrue(self.dxcc_all.removewae())

    def test_correctdata(self):
        self.assertEqual(self.dxcc_all.correctdata("A4", "YG0[54]"), ("A4", "YG0[54]"))
        self.assertEqual(
            self.dxcc_all.correctdata("AA4", "YG0[54]"), ("AA4", "YG0[54]")
        )
        self.assertEqual(self.dxcc_all.correctdata("A4", "YG0(54)"), ("A4", "YG0(54)"))
        self.assertEqual(self.dxcc_all.correctdata("A4", "YG0{54}"), ("A4", "YG0{54}"))

    def test_read(self):
        self.assertGreater(self.dxcc_all.read(), 400)

    # def test_show(self):
    #    self.assertEqual(self.dxcc_all.show("A45wg"), None)

    # def test_showall(self):
    #    self.assertIsInstance(self.dxcc_all.showall(), None)

    def test_std_call(self):
        self.assertEqual(self.dxcc_all.std_call("M0FGC/du3"), None)
        self.assertEqual(self.dxcc_all.std_call("du3/M0FGC"), None)
        self.assertEqual(self.dxcc_all.std_call("M0FGC"), "M0FGC")

    def test_find(self):
        self.assertIsNotNone(self.dxcc_all.find("A45WG"))
        self.assertIsNotNone(self.dxcc_all.find("DU3TIM"))
        self.assertIsNotNone(self.dxcc_all.find("M0FGC"))

    def test_country_name(self):
        self.assertEqual(self.dxcc_all.find("M0FGC").Country_Name, "England")
        self.assertEqual(self.dxcc_all.find("GM0FGC").Country_Name, "Scotland")
        self.assertEqual(self.dxcc_all.find("DU20FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU1FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU1FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU3FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU4FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU5FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU6FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU7FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU8FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("DU9FGC").Country_Name, "Philippines")
        self.assertEqual(self.dxcc_all.find("F0FGC").Country_Name, "France")
        self.assertEqual(self.dxcc_all.find("JA1BOB").Country_Name, "Japan")
        self.assertEqual(self.dxcc_all.find("BD1CNY").Country_Name, "China")
        self.assertEqual(self.dxcc_all.find("K1BOB").Country_Name, "United States")
        self.assertEqual(self.dxcc_all.find("K2BOB").Country_Name, "United States")
        self.assertEqual(self.dxcc_all.find("K3BOB").Country_Name, "United States")
        self.assertEqual(self.dxcc_all.find("K4BOB").Country_Name, "United States")
        self.assertEqual(self.dxcc_all.find("K5BOB").Country_Name, "United States")
        self.assertEqual(self.dxcc_all.find("KH6BOB").Country_Name, "Hawaii")
        self.assertEqual(self.dxcc_all.find("LU2BOB").Country_Name, "Argentina")

    def test_continent(self):
        self.assertEqual(self.dxcc_all.find("M0FGC").Continent_Abbreviation, "EU")
        self.assertEqual(self.dxcc_all.find("GM0FGC").Continent_Abbreviation, "EU")
        self.assertEqual(self.dxcc_all.find("DU20FGC").Continent_Abbreviation,"OC")
        self.assertEqual(self.dxcc_all.find("DU1FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU1FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU3FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU4FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU5FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU6FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU7FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU8FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("DU9FGC").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("F0FGC").Continent_Abbreviation, "EU")
        self.assertEqual(self.dxcc_all.find("JA1BOB").Continent_Abbreviation, "AS")
        self.assertEqual(self.dxcc_all.find("BD1CNY").Continent_Abbreviation, "AS")
        self.assertEqual(self.dxcc_all.find("K1BOB").Continent_Abbreviation, "NA")
        self.assertEqual(self.dxcc_all.find("K2BOB").Continent_Abbreviation, "NA")
        self.assertEqual(self.dxcc_all.find("K3BOB").Continent_Abbreviation, "NA")
        self.assertEqual(self.dxcc_all.find("K4BOB").Continent_Abbreviation, "NA")
        self.assertEqual(self.dxcc_all.find("K5BOB").Continent_Abbreviation, "NA")
        self.assertEqual(self.dxcc_all.find("KH6BOB").Continent_Abbreviation, "OC")
        self.assertEqual(self.dxcc_all.find("LU2BOB").Continent_Abbreviation, "SA")

    def test_country_list(self):
        self.assertEqual(self.dxcc_all.countrylist, TestDxccAll.Country_List)