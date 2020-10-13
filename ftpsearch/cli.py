import click
from ftpsearch.ftpsearch import main

@click.command()
@click.option('--debug/--no-debug', default=False)
@click.option('--query', default='230 country:"AT" port:"21"')
@click.option('--apikey', envvar='SHODAN_API')
def cli(debug, query, apikey):
  """CLI Entrypoint."""
  main(debug=debug, query=query, api_key=apikey)


if __name__ == '__main__':
  cli() # pylint: disable=all
