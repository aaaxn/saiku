# geracao do resumo no terminal e exportacao dos resultados (csv/json/markdown)

from typing import List

import pandas as pd
import typer

FORMATOS = ("csv", "json")


def imprimir_resumo(repo: str, resultado: dict) -> None:
    typer.secho(f"\n Resumo da análise: {repo} ===", bold=True)

    typer.secho("\nIndicadores:", bold=True)
    for nome, valor in resultado["indicadores"].items():
        typer.echo(f"  {nome.replace('_', ' ')}: {valor}")

    typer.secho("\nSinais de manutenção:", bold=True)
    for sinal in resultado["sinais"]:
        typer.secho(f"  ! {sinal}", fg=typer.colors.YELLOW)

    _imprimir_top(
        resultado["issues_antigas"],
        "Issues abertas há mais tempo",
        ["numero", "dias_aberta", "titulo"],
    )
    _imprimir_top(
        resultado["prs_demorados"],
        "PRs mais demorados",
        ["numero", "dias_para_fechar", "titulo"],
    )
    _imprimir_top(
        resultado["arquivos_quentes"],
        "Arquivos mais alterados em correções",
        ["arquivo", "correcoes", "alteracoes"],
    )


def _imprimir_top(
    df: pd.DataFrame, titulo: str, colunas: List[str], n: int = 5
) -> None:
    if df.empty:
        return
    typer.secho(f"\n{titulo} (top {min(n, len(df))}):", bold=True)
    typer.echo(df[colunas].head(n).to_string(index=False, max_colwidth=70))
