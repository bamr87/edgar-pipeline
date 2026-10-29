# edgar-pipeline

> Data pipeline for SEC EDGAR filings: Dagster orchestration, dbt models on DuckDB, MLflow experiments; feeds fredgar-ai and law-ai.

A modern data stack in miniature: ingest EDGAR filings, model them with dbt on DuckDB, orchestrate with Dagster, and track ML experiments in MLflow.

**Status:** foundation (phase 1). Part of the [bamr87 fleet](https://github.com/bamr87/bamr87).

## Goals

- Incremental EDGAR ingestion respecting SEC fair-access rules
- dbt models for companies, filings and XBRL facts on DuckDB
- MLflow-tracked models whose outputs feed fredgar-ai and law-ai

## Skills learned

- Data orchestration with Dagster assets
- dbt modeling and tests
- DuckDB analytics
- ML experiment tracking with MLflow

## Fleet tie-in

Upstream data source for bamr87/fredgar-ai (financial facts) and bamr87/law-ai (filing text).

## Quick start

```bash
pip install -e .[dev] && pytest
```

## How it grows

The roadmap lives in [PRD.md](PRD.md) and [features/features.yml](features/features.yml) (ids `EDGP-NNN`, most `status: planned`). Work arrives as pull requests from the hub's evolution and fan-out loops, the `@claude` handler, or the local `evolve` lane (off until `EVOLVE_ENABLED=true`). A human merges every PR. Rules: [docs/constitution.md](docs/constitution.md) · agent guide: [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)
