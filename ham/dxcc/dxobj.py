import logging
import os
import re


class DxObj(object):
    def __init__(
        self,
        call_starts,
        country_name,
        cq_zone,
        itu_zone,
        continent_abbreviation,
        latitude,
        longitude,
        local_time_offset,
    ):
        """
        Create a Country - note this is using the CallSign Prefix
        :param call_starts:
        param Country_Name:
        :param cq_zone:
        :param itu_zone:
        :param continent_abbreviation:
        :param latitude:
        :param longitude:
        :param local_time_offset:
        :return:
        """
        self._Call_Starts = call_starts
        self._Country_Name = country_name
        self._CQ_Zone = cq_zone
        self._ITU_Zone = itu_zone
        self._continent_abbreviation = continent_abbreviation
        self._Latitude = latitude
        self._Longitude = longitude
        self._Local_time_offset = local_time_offset
        self.logger = logging.getLogger(__name__)

    def show(self):
        print(
            str.format(
                "Country {}:\n\tCQ\t{}\n\tITU\t{}\n\tAbbv\t{}\n\t\tPos\n\t\t\tLat\t{}\n\t\t\tLon\t{}\n\tTZ\t{}",
                self._Country_Name,
                self._CQ_Zone,
                self._ITU_Zone,
                self._continent_abbreviation,
                self._Latitude,
                self._Longitude,
                self._Local_time_offset,
            )
        )

    def dump(self):
        return str.format(
            "Country {}:\n\tCQ\t{}\n\tITU\t{}\n\tAbbv\t{}\n\t\tPos\n\t\t\tLat\t{}\n\t\t\tLon\t{"
            "}\n\tTZ\t{}",
            self._Country_Name,
            self._CQ_Zone,
            self._ITU_Zone,
            self._continent_abbreviation,
            self._Latitude,
            self._Longitude,
            self._Local_time_offset,
        )

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
    def Continent_Abbreviation(self):
        return self._continent_abbreviation

    @property
    def Latitude(self):
        return self._Latitude

    @property
    def Longitude(self):
        return self._Longitude

    @property
    def Local_time_offset(self):
        return self._Local_time_offset