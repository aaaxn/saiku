# TP: Mineração de Repositórios de Software

## Membros do grupo

- Artur Xavier
- Flávio Soriano
- Victoria Flores

## Explicação do sistema

O sistema proposto é uma ferramenta de linha de comando para identificar possíveis problemas de manutenção em repositórios de software.

A ideia principal é analisar o histórico Git de um projeto e encontrar arquivos que podem exigir mais atenção dos desenvolvedores. Para isso, a ferramenta pode observar informações como quantidade de commits por arquivo, frequência de mudanças, número de linhas adicionadas e removidas e complexidade do código.

Com base nessas informações, o sistema gera um ranking dos arquivos mais críticos do repositório. Esses arquivos podem indicar pontos que precisam de revisão, refatoração, mais testes ou acompanhamento durante a manutenção do projeto.

## Possíveis tecnologias utilizadas

- **Python**: linguagem principal para implementar a ferramenta.
- **Typer**: biblioteca para criar a interface de linha de comando.
- **PyDriller**: biblioteca para minerar o histórico Git dos repositórios.
- **Lizard**: ferramenta para calcular métricas de código, como complexidade.
- **Pandas**: biblioteca para organizar e processar os dados coletados.
- **CSV/JSON**: formatos possíveis para exportar os resultados da análise.
