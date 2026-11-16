# Plano — telecom-market-pt (6 semanas)

Plano completo e checklists: ver o documento "Plano Databricks — telecom-market-pt (6 semanas)" no Claude.

## Objetivo

Em 6 semanas ter este repositório público no GitHub com um pipeline Databricks completo
(bronze → silver → gold), um job agendado, um dashboard e um README em inglês.
No fim, decidir se marco o exame Databricks Data Engineer Associate.

## Regras

- 3 sessões de ~1h30 à noite (seg, ter, qui) + sábado de manhã para fechar o entregável.
- Cada semana termina com um commit publicável. Sem commit, a semana não conta.
- Passos pela ordem. Erro ou dúvida → colar no Claude antes de avançar.
- Conteúdo do repositório em inglês; este plano em português.

## Fora do âmbito (até à semana 6)

- BigQuery, dbt, Terraform, Looker Studio → versão 2.
- Post no LinkedIn/blog → só depois de publicar.
- Outros datasets da ANACOM.

## Entregáveis por semana

| Semana | Entregável | Conceitos |
| --- | --- | --- |
| 1 | `01_bronze` carrega os 2 CSVs para Delta; repo no GitHub | Catalog, Volumes, spark.read, Delta |
| 2 | `02_silver` com tipos, nomes limpos, sem duplicados | DataFrames PySpark, functions |
| 3 | `03_gold` com window functions; MERGE incremental na silver | Databricks SQL, MERGE, time travel |
| 4 | Job agendado bronze→silver→gold→quality; `04_quality_checks` | Jobs, dependências, parâmetros |
| 5 | Dashboard AI/BI + README final | SQL Editor, dashboards, escrita técnica |
| 6 | Portfólio, LinkedIn, CV; decisão sobre o exame | — |

## Necessidades

- [x] Conta Databricks Free Edition
- [ ] CSVs `IndI_P070` (móvel) e `IndI_P041` (internet fixa) da ANACOM → guardar em `data/raw/` (não vai para o git)
- [ ] Repositório `telecom-market-pt` público no GitHub (`rodhipolito`)
- [ ] Token pessoal do GitHub para ligar o Databricks (nunca guardar neste repo)
- [ ] Guia oficial do exame Data Engineer Associate, versão 4 maio 2026

## Estrutura da pasta

```
telecom-market-pt/
├── README.md              # em inglês, para recrutadores
├── PLANO.md               # este ficheiro
├── .gitignore
├── notebooks/
│   ├── 01_bronze.py
│   ├── 02_silver.py
│   ├── 03_gold.sql
│   └── 04_quality_checks.py
├── docs/                  # dashboard.png, job_run.png
└── data/raw/              # CSVs locais (ignorados pelo git)
```
