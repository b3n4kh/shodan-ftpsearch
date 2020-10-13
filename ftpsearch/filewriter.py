import os
import json


class Filewriter:
  def __init__(self, filename):
    """
    Filewriter for filename
    """
    dir_name = "data/{0}".format(filename)
    if os.path.isdir(dir_name):
      self.existed = True
    else:
      self.existed = False
      os.mkdir(dir_name)
    self.filename = filename
    self.file = open("data/{0}/intel.txt".format(filename), "a")

  def writeupload(self):
    with open("data/{0}/upload".format(self.filename), "a"):
      pass

  def writeshodan(self, data):
    with open("data/{0}/shodan.json".format(self.filename), "a") as shodan_file:
      shodan_file.write(json.dumps(data, indent=4, sort_keys=True))

  def writeintel(self, data):
    self.file.write("{0}\n".format(data))
