import logging
import sys
import datetime
import time
from enum import Enum

__author__ = 'timseed'


class beaconFld(Enum):
    """
    Create 3 Enums using a range
    """
    call, location, freq = range(3)


class beacon(object):
    freq = [14.1, 18.11, 21.15, 24.930, 28.2]  # in Mhz

    def __init__(self, CALL, Country, b14, b18, b21, b24, b28, Owner, status):
        self.CALL = CALL
        self.Country = Country
        self.band_time = []
        self.band_time.append(beacon.time_str_to_secs(b14))
        self.band_time.append(beacon.time_str_to_secs(b18))
        self.band_time.append(beacon.time_str_to_secs(b21))
        self.band_time.append(beacon.time_str_to_secs(b24))
        self.band_time.append(beacon.time_str_to_secs(b28))
        self.Owner = Owner
        self.status = status
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def time_str_to_secs(tstr):

        '''
        Replace Time_Str to seconds
        :param tstr:  In format of Min:Secs
        :return: int time_in_seconds
        '''
        try:
            min, sec = tstr.split(':')
            return int(min) * 60 + int(sec)
        except:
            return -1


class beacons(object):
    # Some Signals we want to send from this class
    freq = [14.1, 18.11, 21.15, 24.930, 28.2]  # in Mhz
    bands = [14, 18, 21, 24, 28]  # in Mhz
    ref_datetime = datetime.datetime(2016, 1, 1, 0, 0, 1)
    ALL_BANDS=-1

    def __init__(self, ScreenOutput=False):
        self.logger = logging.getLogger(__name__)
        self.selected_band = beacons.ALL_BANDS  # Means ALL BANDS
        self.beacons = []
        self.ScreenOutput = ScreenOutput
        # Setup the Beacon Definitions
        self.beacons.append(beacon('U1UN', 'United Nations', '00:00', '00:10', '00:20', '00:30', '00:40', 'UNRC', 'OK'))
        self.beacons.append(beacon('VE8AT', 'Canada', '00:10', '00:20', '00:30', '00:40', '00:50', 'RAC/NARC', 'OK'))
        self.beacons.append(beacon('W6WX', 'United States', '00:20', '00:30', '00:40', '00:50', '01:00', 'NCDXF', 'OK'))
        self.beacons.append(beacon('KH6RS', 'Hawaii', '00:30', '00:40', '00:50', '01:00', '01:10', 'Maui ARC', 'OFF9'))
        self.beacons.append(beacon('ZL6B', 'New Zealand', '00:40', '00:50', '01:00', '01:10', '01:20', 'NZART', 'OK'))
        self.beacons.append(beacon('VK6RBP', 'Australia', '00:50', '01:00', '01:10', '01:20', '01:30', 'WIA', 'OFF4'))
        self.beacons.append(beacon('JA2IGY', 'Japan', '01:00', '01:10', '01:20', '01:30', '01:40', 'JARL', 'OK'))
        self.beacons.append(beacon('RR9O', 'Russia', '01:10', '01:20', '01:30', '01:40', '01:50', 'SRR', 'OK'))
        self.beacons.append(beacon('VR2B', 'Hong Kong', '01:20', '01:30', '01:40', '01:50', '02:00', 'HARTS', 'OK'))
        self.beacons.append(beacon('4S7B', 'Sri Lanka', '01:30', '01:40', '01:50', '02:00', '02:10', 'RSSL', 'OK'))
        self.beacons.append(beacon('ZS6DN', 'South Africa', '01:40', '01:50', '02:00', '02:10', '02:20', 'ZS6DN', 'OK'))
        self.beacons.append(beacon('5Z4B', 'Kenya', '01:50', '02:00', '02:10', '02:20', '02:30', 'ARSK', 'OK'))
        self.beacons.append(beacon('4X6TU', 'Israel', '02:00', '02:10', '02:20', '02:30', '02:40', 'IARC', 'OK'))
        self.beacons.append(beacon('OH2B', 'Finland', '02:10', '02:20', '02:30', '02:40', '02:50', 'SRAL', 'OK'))
        self.beacons.append(beacon('CS3B', 'Madeira', '02:20', '02:30', '02:40', '02:50', '00:00', 'ARRM', 'OFF4'))
        self.beacons.append(beacon('LU4AA', 'Argentina', '02:30', '02:40', '02:50', '00:00', '00:10', 'RCA', 'OK'))
        self.beacons.append(beacon('OA4B', 'Peru', '02:40', '02:50', '00:00', '00:10', '00:20', 'RCP', 'OK'))
        self.beacons.append(beacon('YV5B', 'Venezuela', '02:50', '00:00', '00:10', '00:20', '00:30', 'RCV', 'OK'))
        self.logger.info("Beacon class initialized")

    def SetBand_in_Mhz(self, band):
        """
        Sets the Band to Specifically to listen too
        Value show be in beacon.Bands

        :param band:  14, 18, 21, 24, 28
        :return:  True/False
        """
        if band in beacons.bands:
            self.selected_band = beacons.bands.index(band)
            self.logger.info(str.format('Band changed to {}', band))
            self.logger.info(str.format('Freq to Listen is {}', self.freq[self.selected_band]))
            self.logger.info(str.format('Freq to Listen is {}', self.freq[self.selected_band]))
            if self.ScreenOutput:
                print('' + (str.format('Band changed to {}', band)))
                print('' + (str.format('Freq to Listen is {}', self.freq[self.selected_band])))
            return True

        else:
            self.selected_band= beacons.ALL_BANDS
            self.logger.error(str.format('Bad Band requested {}', band))
            return False

    def getdelay(self):
        """
        Calculate the delay before the auto detecting mechanism should start
        This should be a delaye of between 0 and 10 seconds only
        :return: time_now, delay_in_Seconds
        """
        tnow = datetime.datetime.now()
        delay = 10.0 - tnow.timestamp() % 10
        self.logger.info(str.format("tnow {}   delay {}", tnow, delay))
        return tnow, delay

    def minsec(self, offset):
        '''
        Return Minute and Seconds offset of Timeslice
        :param offset:
        :return: Tuple (Min,Sec)
        '''
        Min = int(offset / 60)
        Sec = offset - (Min * 60)
        return (Min, Sec)

    def getstation(self):
        """"
        Calculates the Stations which are now active
        TO Restrict. call SetBand(20) before using this method.

        :return: List - each element is a tuple
        Call - Country - Frequency (Mhz)

        """
        ts_now = datetime.datetime.now()
        time_diff = (beacons.ref_datetime - ts_now).seconds
        next_beacon = ('Unk', 'Unk')
        second_in_phase = ts_now.timestamp() % 180
        self.logger.info("Seconds in Phase = %d" % second_in_phase)
        next_active = (((int(second_in_phase / 10)) * 10) + 0) % 180
        OSet = self.minsec(next_active)
        self.logger.info("Next Active %d in secs is %d Min %d " % (next_active,
                                                                   OSet[0],
                                                                   OSet[1]))

        self.logger.info(str.format('Band {} Seconds {} next {} ',
                                    self.selected_band,
                                    second_in_phase,
                                    next_active))
        next_station = []
        if self.selected_band != -1:
            for b in self.beacons:
                if self.selected_band != -1 and b.band_time[self.selected_band] == next_active:
                    self.logger.info(str.format('Band time Index {}  {}',
                                                b.CALL,
                                                b.band_time[self.selected_band]))
                    next_beacon = (b.CALL, b.Country, beacon.freq[self.selected_band])
                    next_station.append(next_beacon)
                    # We are in Single Band Mode - find one and quit this loop
                    break
        else:
            for band in range(5):
                for b in self.beacons:
                    if b.band_time[band] == next_active:
                        next_beacon = (b.CALL, b.Country, beacon.freq[band])
                        next_station.append(next_beacon)
                        break

        return next_station

    def beacon_start(self, timeout=30):
        tnow, delay = self.getdelay()
        self.logger.info(str.format('timenow is {}', tnow.timestamp()))
        self.logger.info(str.format('delay   is {}', delay))
        while (timeout > 0):
            timeout = timeout - delay
            next_station = self.getstation()  # Returns an Array of Stations
            self.logger.info("--------------")
            for ns in next_station:
                self.logger.info(str.format('Call {} Country {} Freq {}',
                                            ns[beaconFld.call.value],
                                            ns[beaconFld.location.value],
                                            ns[beaconFld.freq.value]))
                if self.ScreenOutput:
                    print('' + str.format('Call {} Country {} Freq {}',
                                          ns[beaconFld.call.value],
                                          ns[beaconFld.location.value],
                                          ns[beaconFld.freq.value]))

            time.sleep(delay)
            tnow, delay = self.getdelay()
        self.logger.info('Loop run ended')


    def dump_band(self, band_id):
        """
        Debugging Routine

            This is output to the logger not returned as a string.

        :param band_id: Band index (0-4)
        :return:    None
        """
        self.logger.info(str.format('Dumping Band ID {}', band_id))
        for b in self.beacons:
            self.logger.info(str.format('Time offset {} ', b.band_time[band_id]))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    dx = beacons()
    # dx.SetBand(int(sys.argv[1]))
    dx.beacon_start(timeout=5000)
    dx.dump_band(4)
    junk = 1
    junk = 1
