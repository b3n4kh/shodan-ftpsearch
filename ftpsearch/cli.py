import click
from ftpsearch.ftpsearch import main

@click.command()
@click.option('--debug/--no-debug', default=True)
@click.option('--port', default=21, show_default=True)
@click.option('--country', default='AT', show_default=True, help="Country Code")
@click.option('--rcode', default=230, show_default=True, help="FTP server return code")
@click.option('--output', default='data', show_default=True)
@click.option('--apikey', envvar='SHODAN_API')
def cli(debug, port, country, rcode, output, apikey):
  """CLI Entrypoint."""
  query = '{0} country:"{1}" port:"{2}"'.format(rcode, country, port)

  main(debug=debug, query=query, api_key=apikey, output=output)


if __name__ == '__main__':
  cli() # pylint: disable=all
