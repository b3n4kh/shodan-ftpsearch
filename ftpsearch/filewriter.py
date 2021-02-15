import os
import json


class Filewriter:
  def __init__(self, basefolder: str, filename: str):
    """
    Filewriter for filename
    """
    dir_name = "{0}/{1}".format(basefolder, filename)
    if os.path.isdir(dir_name):
      self.existed = True
    else:
      self.existed = False
      os.mkdir(dir_name)
    self.filename = filename
    self.basepath = dir_name
    self.intel = open("{0}/intel.txt".format(dir_name), "a")

  def writeupload(self):
    with open("{0}/upload".format(self.basepath), "a"):
      pass

  def writeshodan(self, data):
    with open("{0}/shodan.json".format(self.basepath), "a") as shodan_file:
      shodan_file.write(json.dumps(data, indent=4, sort_keys=True))

  def writeintel(self, data):
    self.intel.write("{0}\n".format(data))
