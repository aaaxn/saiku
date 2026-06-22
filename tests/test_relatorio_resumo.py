# teste de que o resumo no terminal nao quebra e imprime os indicadores
from saiku import analise, relatorio


def test_imprimir_resumo_nao_lanca(capsys, issues, prs, arquivos):
    res = analise.analisar(issues, prs, arquivos)
    relatorio.imprimir_resumo("dono/repo", res)
    saida = capsys.readouterr().out
    assert "Indicadores" in saida
