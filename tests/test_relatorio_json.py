# teste da exportacao dos resultados em json
import json

from saiku import analise, relatorio


def test_exportar_json(tmp_path, issues, prs, arquivos):
    res = analise.analisar(issues, prs, arquivos)
    gerados = relatorio.exportar(tmp_path, "json", issues, prs, arquivos, res)
    assert len(gerados) == 1
    dados = json.loads(gerados[0].read_text(encoding="utf-8"))
    assert dados["indicadores"]["issues_analisadas"] == 5
