from shodan import Shodan
from ftplib import FTP
from ftpsearch.filewriter import Filewriter
import ftplib
import logging
import io



def ftpupload(ftp: FTP) -> bool:
  try:
    bio = io.BytesIO(b'Anon writes')
    ftp.storbinary('STOR upload.txt', bio)
  except ftplib.all_errors as e:
    logging.debug('Ftp upload failed -> {0}'.format(e))
    return False
  return True


def ftplogin(ip: str) -> FTP:
  try:
    ftp = FTP(ip)
    ftp.login()
  except ftplib.all_errors as e:
    logging.debug('Ftp login failed -> {0}'.format(e))
    return None
  return ftp


def shodan_search(query: str, api: Shodan):
  """
  Search Shodan for query
  """
  for matches in api.search_cursor(query):
    ip_addr = matches['ip_str']
    fw = Filewriter(ip_addr)
    if fw.existed:
      continue
    ftp = ftplogin(ip_addr)
    if ftp != None:
      fw.writeshodan(matches)
      try:
        ftp.retrlines('LIST', callback=fw.writeintel)
      except ftplib.all_errors as e:
        logging.debug('Ftp LIST failed -> {0}'.format(e))
        continue
      if ftpupload(ftp):
        fw.writeupload()


def main(debug: bool, query: str, api_key: str):
  api = Shodan(api_key)
  if debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)

  shodan_search(query, api)

