from click.testing import CliRunner

from oddsbot.cli import cli


def test_cli_list_sports():
    runner = CliRunner()
    result = runner.invoke(cli, ["list-sports"])
    assert result.exit_code == 0
