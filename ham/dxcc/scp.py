import logging
import datetime
import os
import ham.dxcc

class SCP(object):

  def __init__(self):
    self.logger = logging.getLogger(__name__)
    formatter = logging.Formatter(
          "[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
          "%m-%d %H:%M:%S",
      )
    _data = []
    wanted_file = (
        os.path.join(os.path.dirname(ham.dxcc.__file__), "data") + "/MASTER.SCP"
    )
    self.load(wanted_file)

  def load(self, fname:str) -> list:
      with open(fname,'rt') as ifp:
          self._data=ifp.read().split('\n')
      return self.Data

  @property
  def Data(self) -> list:
      return self._data

  @property
  def count(self) -> int:
      return len(self._data)
