# teste do tratamento de formato invalido na cli
from typer.testing import CliRunner

from saiku.main import app

runner = CliRunner()


def test_formato_invalido_sai_com_erro():
    resultado = runner.invoke(app, ["dono/repo", "--formato", "xml"])
    assert resultado.exit_code == 1
