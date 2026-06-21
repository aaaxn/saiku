# teste de coletar_arquivos_de_correcoes com objetos simulados
from saiku import coleta


class _Arquivo:
    def __init__(self, filename, changes):
        self.filename = filename
        self.changes = changes


class _PR:
    def __init__(self, numero, arquivos):
        self.number = numero
        self._arquivos = arquivos

    def get_files(self):
        return self._arquivos


def test_lista_arquivos_das_correcoes():
    correcoes = [_PR(1, [_Arquivo("a.py", 10), _Arquivo("b.py", 3)])]
    dados = coleta.coletar_arquivos_de_correcoes(correcoes, 15)
    assert len(dados) == 2
    assert dados[0] == {"pr": 1, "arquivo": "a.py", "alteracoes": 10}


def test_respeita_o_limite_de_prs():
    correcoes = [_PR(i, [_Arquivo("x.py", 1)]) for i in range(5)]
    dados = coleta.coletar_arquivos_de_correcoes(correcoes, 2)
    assert len(dados) == 2  # so dois prs inspecionados
