# telecom-market-pt

Tracks mobile and fixed broadband market share in Portugal using ANACOM open data, built as a Databricks lakehouse pipeline (bronze → silver → gold).

> Status: in progress — week 1 of 6.

![Dashboard](docs/dashboard.png)

## Architecture

```
ANACOM CSV → Volume (raw) → bronze → silver → gold → AI/BI dashboard
```

| Layer | What it does | Table(s) |
| --- | --- | --- |
| Bronze | Raw CSV loaded as-is into Delta | `bronze_mobile_share`, `bronze_fixed_internet_share` |
| Silver | Typed columns, clean names, deduplicated, incremental MERGE | `silver_mobile_share`, `silver_fixed_internet_share` |
| Gold | Business tables: share change, rank, leader gap | `gold_market_share_quarterly`, `gold_leader_by_period` |

## Tech stack

Databricks Free Edition · Delta Lake · PySpark · Databricks SQL · Databricks Jobs

## Data quality

Four checks run as the last task of the job and fail the run if any breaks:
no null operator · share between 0 and 100 · period totals ≈ 100 · no duplicate keys.

## How to run

1. In Databricks, create schema `workspace.telecom` and volume `raw`.
2. Upload `IndI_P070.csv` and `IndI_P041.csv` from the ANACOM open data portal to the volume.
3. Run the job `telecom-market-pt-pipeline` (bronze → silver → gold → quality).

## What I learned

_TODO — fill in week 5._

## Next steps

- Automated ingestion from ANACOM
- Lakeflow Declarative Pipelines
- dbt transformation layer
