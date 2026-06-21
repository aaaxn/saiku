# testes da classificacao de bugs por palavras-chave
import pytest

from saiku import coleta


@pytest.mark.parametrize(
    "titulo",
    ["Corrige crash ao salvar", "Bug no login", "hotfix urgente", "Fix typo"],
)
def test_titulos_de_bug(titulo):
    assert coleta._eh_bug(titulo, []) is True


def test_titulo_comum_nao_eh_bug():
    assert coleta._eh_bug("Adiciona nova pagina", []) is False


def test_label_marca_como_bug():
    assert coleta._eh_bug("Tarefa qualquer", ["bug"]) is True
