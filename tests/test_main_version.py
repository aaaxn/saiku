# teste da flag --version da cli
from typer.testing import CliRunner

from saiku.main import app

runner = CliRunner()


def test_version_mostra_nome_e_sai():
    resultado = runner.invoke(app, ["--version"])
    assert resultado.exit_code == 0
    assert "saiku" in resultado.output
