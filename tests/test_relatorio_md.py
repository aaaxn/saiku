# teste da exportacao do resumo em markdown
from saiku import analise, relatorio


def test_exportar_markdown(tmp_path, issues, prs, arquivos):
    res = analise.analisar(issues, prs, arquivos)
    gerados = relatorio.exportar(tmp_path, "md", issues, prs, arquivos, res)
    assert gerados[0].name == "analise.md"
    texto = gerados[0].read_text(encoding="utf-8")
    assert texto.startswith("# Resumo da analise")
    assert "## Indicadores" in texto
