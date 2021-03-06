import re
import pprint
import pkg_resources


class dxcc(object):

    def __init__(self, Call_Starts, Country_Name, CQ_Zone,
                 ITU_Zone, continent_abbreviation, Latitude, Longitude,
                 Local_time_offset):

        self._Call_Starts = Call_Starts
        self._Country_Name = Country_Name
        self._CQ_Zone = CQ_Zone
        self._ITU_Zone = ITU_Zone
        self._continent_abbreviation = continent_abbreviation
        self._Latitude = Latitude
        self._Longitude = Longitude
        self._Local_time_offset =Local_time_offset

    def show(self):
        print('{0}'.format(self.dump())
              )

    def dump(self):
        return str.format(
            'Country {}:\n\tCQ\t{}\n\tITU\t{}\n\tAbbv\t{}\n\t\tPos\n\t\t\tLat\t{}\n\t\t\tLon\t{}\n\t',
            self._Country_Name,
            self._CQ_Zone,
            self._ITU_Zone,
            self._continent_abbreviation,
            self._Latitude,
            self._Longitude,
        )


    def Call_Starts(self):
        return self._Call_Starts

    @property
    def Country_Name(self):
        return self._Country_Name

    @property
    def CQ_Zone(self):
        return self._CQ_Zone

    @property
    def ITU_Zone(self):
        return self._ITU_Zone

    @property
    def continent_abbreviation(self):
        return self._continent_abbreviation


    def Latitude(self):
        return float(self._Latitude)


    def Longitude(self):
        return float(self._Longitude)

    @property
    def Local_time_offset(self):
        return self._Local_time_offset


class dxcc_all(object):
    def __init__(self):
        self._dxcclist = {}

    def RemoveWAE(self):
        """
        Some prefixes exist only for WAE
        :return:
        """

    def __len__(self):
        return len(self._dxcclist)

    def correctdata(self, prefix, DxRec):
        """
        (#)	Override CQ Zone
        [#]	Override ITU Zone
        <#/#>	Override latitude/longitude
        {aa}	Override Continent
        ~#~	Override local time offset from GMT

        i.e. YG0[54] means Override the ITU Zone

        :rtype: object
        :param DxRec:
        :return: prefix, DxRec
        """
        if prefix == "ZL5(30)[71]":
            junk = 1
        prefix = prefix.replace(' ', '')
        m = re.search('[^A-Za-z0-9]', prefix)
        if m != None:
            # print("Prefix is Special "+prefix)
            if prefix.startswith('='):
                print("Specific Call")
                prefix = prefix.replace('=', '')
            mCQ = re.search('(\([0-9]+\))', prefix)
            if mCQ != None:
                # CQ Zone Change
                newCqZone = mCQ.groups(0)[0]
                print(str.format("{} has CQZone Change {}", prefix, newCqZone))
                prefix = prefix.replace(newCqZone, '')
                newCqZone = newCqZone.replace('(', '').replace(')', '')
                # Make new tuple
                #
                x = (newCqZone,)
                DxRec = (DxRec[:1] + x + DxRec[2:])
            mITU = re.search('(\[[0-9]+\])', prefix)
            if mITU != None:
                newITUZone = mITU.groups(0)[0]
                print(str.format("{} has ITU Change {}", prefix, newITUZone))
                prefix = prefix.replace(newITUZone, '')
                newITUZone = newITUZone.replace('[', '').replace(']', '')
                # Make new tuple
                #
                x = (newITUZone,)
                DxRec = (DxRec[:2] + x + DxRec[3:])
            mCONT = re.search('({[0-9]+})', prefix)
            if mCONT != None:
                newCont = mCONT.groups(0)[0]
                print(str.format("{} has ITU Change {}", prefix, newCont))
                prefix = prefix.replace(newCont, '')
                newCont = newCont.replace('{', '').replace('}', '')
                # Make new tuple
                #
                x = (newCont,)
                DxRec = (DxRec[:3] + x + DxRec[4:])

        return prefix, DxRec

    def read(self):
        self._dxcclist = {}
        try:
            from inspect import getsourcefile
            from os import chdir
            from os.path import abspath, dirname

            where_are_we = dirname(abspath(getsourcefile(lambda: 0)))

            txt = open(where_are_we + "/cty.dat").read()
            element = txt.split(';')
            for e in element:
                if len(e) > 0:
                    try:
                        parts = tuple([a.rstrip(' ').lstrip(' ').replace('\n', '') for a in e.split(':')])
                        prefix = str(parts[8]).rstrip(' ').lstrip(' ')

                        for p in prefix.split(','):
                            try:
                                tmp_parts = parts[0:7]
                                clean_prefix, tmp_parts_2 = self.correctdata(p, tmp_parts)
                                d = dxcc(Call_Starts=clean_prefix,
                                         Country_Name=tmp_parts_2[0],
                                         CQ_Zone=tmp_parts_2[1],
                                         ITU_Zone=tmp_parts_2[2],
                                         continent_abbreviation=tmp_parts_2[3],
                                         Latitude=tmp_parts_2[4],
                                         Longitude=tmp_parts_2[5],
                                         Local_time_offset=tmp_parts_2[6])

                                self._dxcclist[clean_prefix] = d
                                print("Array has ", str(len(self._dxcclist)))
                            except IndexError:
                                print("Error" + str(e))
                                pass
                            except Exception as e:
                                print("Some other error " + str(e))
                    except IndexError:
                        print("Error" + e)
                        pass
                    except:
                        print("Some other error")
        except FileNotFoundError:
            print("File Opening Error")
            exit(1)


    def show(self, dx_station):

        for dx in self._dxcclist:
            if dx_station.startswith(dx):
                self._dxcclist[dx].show()
                return self._dxcclist[dx]
        return None

   
    def showall(self):
        for a in sorted(self._dxcclist):
            self._dxcclist[a].show()

    def std_call(self, call):
        """
        try and fix a callsign that can be entered like this du2/m0fgc/p or m0fgc/du2 or m0fgc/p
        Is
            * English Call
            * In Philippines

        :param call:
        :return:

        """
        cs = '/'.join(sorted(call.upper().split('/'), key=len, reverse=True))

        cnt = cs.count('/')
        if cnt == 0:
            # No /'s
            return cs
        elif cnt == 1:
            # m0fgc/p or du2/m0fgc
            # EEK
            help = 1

    def find(self, call):
        """
        Find the Country to a call sign

        :param call: Full or Partial Call
        :return: Matched DXCC Entity - None if not Found

        """
        match = None
        for a in sorted(self._dxcclist):
            if self._dxcclist[a].Call_Starts().startswith(call):
                match = self._dxcclist[a]
                break
        return match


if __name__ == "__main__":
    d = dxcc_all()
    d.read()
    d.showall()
    # d.show('G')
    # d.show('F')
    d.show('M0FGC')
