<!-- kit: governance v0.1.0 -->
# 0002 — Missions

- **Status:** proposed
- **Date:** 2026-11-16
- **Proposed by:** Grok Bot (agent), at the maintainer's request
- **Ratified by:**
- **Affects:** constitution §1; PRD §1.1; feature EDGP-008
- **Supersedes:** none
- **Related:** [PRD.md](../../PRD.md) §1.1; feature EDGP-008

## Context

Constitution §1 Mission was a product description (or, for a new constitution, had not been written yet), not a three-mission direction statement. The fleet now requires every repo's constitution §1 to be one direction statement followed by exactly three numbered missions, adopted through a numbered amendment the maintainer ratifies by merging. The maintainer asked for those missions to be comprehensive and epic: EDGAR Pipeline as the ultimate open home for all things SEC EDGAR data pipelines. Mission 1 follows the maintainer's wording, adapted to this domain: provide data, tools, resources and transparency for all stakeholders, domain practitioners and the general public. The ambition is the direction, not a claim that the work is already finished. The missions are aligned with this repo's existing constitution and PRD.

## Amendment

Replace constitution §1 with the following, retitled **Missions**:

EDGAR Pipeline's direction is to become the ultimate open home for all things SEC EDGAR data pipelines — data, tools, resources and transparency, gathered in one place that anyone can inspect and reuse.

1. **Provide data, tools, resources and transparency for all stakeholders, finance and data professionals, and the general public.** Analysts, researchers, downstream product builders and anyone studying public filings are first-class audiences. The aim is a shared, inspectable commons: the same filings, the same models, and the same trail from source document to structured fact for everyone.
2. **Ingest, model and orchestrate public EDGAR filings as a reproducible modern data stack that anyone can inspect and rerun.** The path is a learning-first, open pipeline: dbt models on DuckDB, Dagster orchestration, and MLflow experiment tracking, with every step visible in the repository.
3. **Feed downstream open products with a clear, auditable trail: financial facts for fredgar-ai and filing text for law-ai, without blending estimates into reported facts.** The pipeline is a source, not a black box; provenance travels with the data.

These missions set the course; they do not claim the work is finished. They serve the PRD's picture of a modern data stack in miniature and this repo's role as an upstream source for the fleet's financial and legal products.

_Source: [PRD.md](../PRD.md) §1.1._


## Consequences

Agents and reviewers judge fit against these three missions before inventing scope, treating them as the direction of the repo rather than a description of what already ships. The same text is added as PRD §1.1 so the constitution's `_Source:` line stays accurate. The original PRD purpose / overview paragraph is left in place. This PR also aligns the README and AGENTS.md taglines with the missions and links them to constitution §1, and adds feature EDGP-008 to the feature catalog, traced to requirement MR1. Merging this PR ratifies amendment 0002. Until then the record stays `Status: proposed`.
