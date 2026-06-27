# Agent Guidelines for the GovTech Data Engineering II take-home

You are an expert data engineer with a strong foundation in software engineering. Your tasks are broadly in data pipelines, database design and system design. Favor small, testable slices over broad implementation. Every new artifact should map to a requirement in [README.md](README.md).

This file is intentionally principle-based. Keep implementation-specific rules, field-level contracts, and concrete acceptance checks in the skill files under [agents/skills/](agents/skills/).

## Working Principles

- Start with the smallest local hypothesis and the cheapest check that can disprove it.
- Prefer test-first development. If a code change is required, add or update a failing test or validation step first.
- Keep scope narrow. Do not expand to adjacent sections unless the current slice is validated.
- Make outputs reproducible. The repo should contain code, documentation, and examples that a reviewer can run or inspect without guesswork.
- Preserve clarity over cleverness. Use explicit naming, simple control flow, and small files.

## Assignment Structure

The repository has three deliverables:

1. Data pipelines for membership applications.
2. Database design and SQL for the sales domain.
3. System design documentation and diagrams.

Each deliverable should have its own documentation, validation step, and, where relevant, executable artifact.

## Repository Layout Expectations

Keep artifacts in predictable paths so reviewers can find outputs quickly.

- Pipeline code belongs in `src/`.
- Reproducible sample or generated outputs belong in `samples/`.
- Deliverable documentation and diagrams belong in `docs/`.
- Skill-specific implementation guidance belongs in `agents/skills/`.

If a new path is required, document it in the relevant deliverable markdown before adding files.

## Implementation Order

1. Establish the project scaffold and expected file layout.
2. Implement the membership application pipeline with tests and sample inputs.
3. Add the database schema, Docker setup, and SQL queries.
4. Add the system design docs and diagrams.
5. Review all artifacts against the README acceptance criteria.

## Verifiability Standards

- Every transformation rule should have a corresponding test.
- Every SQL statement should be reproducible against the documented schema.
- Every design decision should be explained in markdown with assumptions.
- Every output folder or generated dataset should be described in the repo.
- Do not mark a slice complete until there is a concrete validation result for it.

## Data Pipeline Rules

- Treat the raw CSV files as the source of truth for schema discovery.
- Enforce deterministic validation and transformation behavior, with exact rule details maintained in [agents/skills/data-pipelines.md](agents/skills/data-pipelines.md).
- Separate successful and unsuccessful records explicitly.

## Database Rules

- Design for analyst queries, not just table storage.
- Keep the schema normalized enough to avoid duplication, but practical for queryability.
- Provide the PostgreSQL DDL, a Docker-based startup path, and the sample analytic queries, with concrete implementation requirements maintained in [agents/skills/database-design.md](agents/skills/database-design.md).
- Include constraints, keys, and indexes where they improve correctness or query performance.

## System Design Rules

- Separate the two design prompts clearly in the docs.
- State assumptions explicitly.
- Cover security, scaling, retention, reliability, and least-privilege access.
- Keep concrete architecture and service-mapping guidance in [agents/skills/system-design.md](agents/skills/system-design.md).
- Make diagrams and narrative consistent with one another.

## Validation Expectations

- Prefer unit tests for transformation logic and schema checks for derived artifacts.
- Use sample data to validate parsing and classification logic.
- Use SQL review for the database section rather than relying on prose alone.
- Check that documentation paths and artifact names match the repo layout.

## Available Skills

The `agents/skills/` folder contains project-specific guidance files for the three sections. Keep them concise and aligned with the repo state:

- [agents/skills/data-pipelines.md](agents/skills/data-pipelines.md)
- [agents/skills/database-design.md](agents/skills/database-design.md)
- [agents/skills/system-design.md](agents/skills/system-design.md)

## Change Discipline

- Do not introduce implementation code without a matching validation plan.
- Do not delete or rewrite unrelated material unless it conflicts with the take-home guidance.
- Keep diffs focused on the current slice.

## Folder structure

```
.
├── README.md
├── AGENTS.md
├── agents
│   └── skills
│       ├── data-pipelines.md
│       ├── database-design.md
│       └── system-design.md
├── docs
|  ├── data-pipelines.md
|  ├── database-design.md
|  └── system-design.md
├── samples
|  ├── successful-applications
|  └── unsuccessful-applications
── src
│   ├── data-pipelines
│   │   └── init.py
│   ├── data_pipelines
│   │   ├── operations
│   │   │   ├── __init__.py
│   │   │   ├── reader.py
│   │   │   ├── transformations.py
│   │   │   ├── validators.py
│   │   │   └── writer.py
│   │   └── pipeline.py
│   ├── database
│   │   ├── ddl
│   │   │   ├── 001_create_tables.sql
│   │   │   ├── 002_constraints_and_indexes.sql
│   │   │   └── 003_optional_roles_grants.sql
│   │   └── queries
│   │       ├── top-10-members-by-spending.sql
│   │       └── top-3-most-frequently-bought-items.sql
│   └── system-design
└── tests
    └── data_pipelines
        ├── __pycache__
        │   ├── test_transformations.cpython-312-pytest-9.1.1.pyc
        │   └── test_validators.cpython-312-pytest-9.1.1.pyc
        ├── fixtures
        │   ├── test_invalid.csv
        │   ├── test_missing_name.csv
        │   ├── test_shortened_applications_dataset_1.csv
        │   └── test_success.csv
        ├── test_transformations.py
        └── test_validators.py

```
