from click.testing import CliRunner

from distri import cli


def test_version_ok():
    runner = CliRunner()
    
    result = runner.invoke(cli.version, [])

    assert result.exit_code == 0
    assert result.output == 'v0.1.0\n'
