import sys

import click
from prettytable import PrettyTable

from . import config, errors


@click.group
def cli() -> None:
    pass


@cli.command
def version() -> None:
    v = '0.1.0'

    click.echo(f'v{v}')


@cli.command
@click.option('--path', default='/etc/os-release', help='os release file path to parse')
def display(path : str) -> None:
    data = config.load(path)

    table = PrettyTable([], header=False, align='l')
    for k,v in data.items():
        table.add_rows([[k, v]])
    
    click.echo(table)


def run() -> None:
    try:
        cli()
    except errors.DistriError as e:
        sys.stderr.write(f'{e}\n')
        sys.exit(e.code)
