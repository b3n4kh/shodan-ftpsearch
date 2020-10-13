import os
import json

class Filewriter:
  def __init__(self, filename):
    """
    Filewriter for filename
    """
    os.mkdir("data/{0}".format(filename))
    self.filename = filename
    self.file = open("data/{0}/intel.txt".format(filename), "a")


  def writeshodan(self, data):
    with open("data/{0}/shodan.json".format(self.filename), "a") as shodan_file:
      shodan_file.write(json.dumps(data, indent=4, sort_keys=True))

  def writeintel(self, data):
    self.file.write("{0}\n".format(data))
