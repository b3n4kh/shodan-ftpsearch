from shodan import Shodan
from ftplib import FTP
from ftpsearch.filewriter import Filewriter
import ftplib
import logging


def test_ftplogin(ip: str):
  try:
    ftp = FTP(ip)  # connect to host, default port
    ftp.login()
  except ftplib.all_errors as e:
    logging.debug('Ftp login failed -> {0}'.format(e))
    return None
  return ftp


def shodan_search(query: str, api):
  """
  Search Shodan for query
  """
  for matches in api.search_cursor(query):
    ftp = test_ftplogin(matches['ip_str'])
    if ftp != None:
      fw = Filewriter(matches['ip_str'])
      fw.writeshodan(matches)
      ftp.retrlines('LIST', callback=fw.writeintel)
    # ftp = save_ftp_list


def main(debug: bool, query: str, api_key: str):
  api = Shodan(api_key)
  if debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)

  shodan_search(query, api)

