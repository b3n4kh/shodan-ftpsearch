import click
from ftpsearch.ftpsearch import main

@click.command()
@click.option('--debug/--no-debug', default=True)
@click.option('--query', default='230 country:"AT" port:"21"', show_default=True)
@click.option('--output', default='data', show_default=True)
@click.option('--apikey', envvar='SHODAN_API')
def cli(debug, query, output, apikey):
  """CLI Entrypoint."""
  main(debug=debug, query=query, api_key=apikey, output=output)


if __name__ == '__main__':
  cli() # pylint: disable=all
