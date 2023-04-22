import json

import pytest
from click.testing import CliRunner
from prettytable import PrettyTable

from distri import cli, errors


def test_display_error_file():
    runner = CliRunner()
    res = runner.invoke(cli.cli, ['display', '--path', '/404'])

    assert res.exit_code == 1
    assert res.output == ''


def test_display_ok(fwd):
    runner = CliRunner()

    with open(f'{fwd}/config/fedora.json', 'r') as f:
        data = json.load(f)
    
    
    table = PrettyTable([], header=False, align='l')
    for k,v in data.items():
        table.add_rows([[k, v]])
    
    current = runner.invoke(cli.display, [])

    assert str(table) + '\n' == current.output
