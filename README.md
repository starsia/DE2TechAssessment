# DE2 Technical Assessment

This repository contains my submission for the DE2 Technical Assessment. The solution is divided into three independent sections:

1. Data Engineering Pipeline (ETL)
2. Database Design
3. System Design

Each section includes implementation, documentation, and supporting scripts.

---

# Repository Structure

```text
.
├── ./AGENTS.md
├── ./README.md
├── ./agents
│   └── ./agents/skills
│       ├── ./agents/skills/data_pipelines.md
│       ├── ./agents/skills/database_design.md
│       └── ./agents/skills/system_design.md
├── ./assets
│   └── ./assets/Section3.2.png
├── ./compose.yaml
├── ./data
│   ├── ./data/output
│   │   ├── ./data/output/20260629_220204
│   │   │   └── ./data/output/20260629_220204/input
│   │   ├── ./data/output/20260629_221130
│   │   │   └── ./data/output/20260629_221130/input
│   │   ├── ./data/output/20260629_221705
│   │   │   └── ./data/output/20260629_221705/input
│   │   └── ./data/output/20260629_222004
│   │       └── ./data/output/20260629_222004/input
│   └── ./data/to_process
│       ├── ./data/to_process/applications_dataset_1.csv
│       └── ./data/to_process/applications_dataset_2.csv
├── ./database
│   ├── ./database/er_diagram
│   │   └── ./database/er_diagram/ER_diagram.png
│   ├── ./database/init
│   │   ├── ./database/init/001_create_tables.sql
│   │   ├── ./database/init/002_constraints_and_indexes.sql
│   │   ├── ./database/init/003_optional_roles_grants.sql
│   │   ├── ./database/init/004_insert_members.sql
│   │   ├── ./database/init/005_insert_manufacturers.sql
│   │   ├── ./database/init/006_insert_items.sql
│   │   ├── ./database/init/007_insert_transactions.sql
│   │   ├── ./database/init/008_insert_transaction_items.sql
│   │   └── ./database/init/009_create_views.sql
│   └── ./database/queries
│       ├── ./database/queries/top-10-members-by-spending.sql
│       └── ./database/queries/top-3-most-frequently-bought-items.sql
├── ./docs
│   ├── ./docs/section1_data_pipelines.md
│   ├── ./docs/section2_database_design.md
│   └── ./docs/section3_system_design.md
├── ./processed_dataset
│   └── ./processed_dataset/20260629_215505
│       ├── ./processed_dataset/20260629_215505/input
│       │   ├── ./processed_dataset/20260629_215505/input/applications_dataset_1.csv
│       │   └── ./processed_dataset/20260629_215505/input/applications_dataset_2.csv
│       ├── ./processed_dataset/20260629_215505/successful.csv
│       └── ./processed_dataset/20260629_215505/unsuccessful.csv
├── ./requirements.txt
├── ./scripts
│   ├── ./scripts/install_cron.sh
│   ├── ./scripts/remove_cron.sh
│   └── ./scripts/run_pipeline.sh
├── ./src
│   ├── ./src/data_pipelines
│   │   ├── ./src/data_pipelines/operations
│   │   │   ├── ./src/data_pipelines/operations/__init__.py
│   │   │   ├── ./src/data_pipelines/operations/constants.py
│   │   │   ├── ./src/data_pipelines/operations/helpers.py
│   │   │   ├── ./src/data_pipelines/operations/reader.py
│   │   │   ├── ./src/data_pipelines/operations/transformations.py
│   │   │   ├── ./src/data_pipelines/operations/validators.py
│   │   │   └── ./src/data_pipelines/operations/writer.py
│   │   └── ./src/data_pipelines/pipeline.py
│   └── ./src/system_design
└── ./tests
    └── ./tests/data_pipelines
        ├── ./tests/data_pipelines/fixtures
        │   ├── ./tests/data_pipelines/fixtures/test_above18.csv
        │   └── ./tests/data_pipelines/fixtures/test_shortened_applications_dataset_1.csv
        ├── ./tests/data_pipelines/test_helpers.py
        ├── ./tests/data_pipelines/test_pipeline.py
        ├── ./tests/data_pipelines/test_transformations.py
        └── ./tests/data_pipelines/test_validators.py

```

---

# Section 1 — Data Pipeline

The first section implements an hourly batch ETL pipeline that processes membership applications.

The pipeline performs the following stages:

- Extracts all CSV files dropped into `data/to_process`
- Consolidates multiple datasets into a single processing batch
- Cleans and transforms applicant information
- Validates applications against the business rules
- Generates membership IDs for successful applicants
- Separates successful and unsuccessful applications
- Stores each execution as an immutable batch

Each pipeline execution produces a timestamped batch:

```text
data/output/

    YYYYMMDD_HHMMSS/

        input/
            applications_dataset_1.csv
            applications_dataset_2.csv

        successful.csv

        unsuccessful.csv
```

This preserves full traceability between processed outputs and their original source files.

### Pipeline Architecture

```
to_process/
      │
      ▼
 Reader (Extract)
      │
      ▼
Pipeline (Transform + Validate)
      │
      ▼
 Writer (Load)
      │
      ▼
output/<timestamp>/
    ├── input/
    ├── successful.csv
    └── unsuccessful.csv
```

### Scheduling

The pipeline is scheduled using **cron** and executes every hour.

Helper scripts are provided:

```text
scripts/
    run_pipeline.sh
    install_cron.sh
    remove_cron.sh
```

Documentation can be found in:

```
docs/section1_data_pipelines.md
```

Processed outputs are stored in:

```
processed_dataset/
    └── <timestamp>/
        ├── input/
        ├── successful.csv
        └── unsuccessful.csv
```

---

# Section 2 — Database Design

The second section designs an OLTP PostgreSQL database for an e-commerce platform.

The schema models:

- Members
- Manufacturers
- Items
- Transactions
- Transaction Items

using Third Normal Form (3NF).

An Entity Relationship Diagram is included to illustrate the data model.

### Features

- PostgreSQL
- Docker Compose deployment
- DDL scripts
- Seed data
- Constraints
- Foreign keys
- Indexes
- Analytical SQL views

The repository also includes SQL solutions for the requested analytical questions:

- Top 10 members by spending
- Top 3 most frequently purchased items

along with an additional example analytical view.

### Database Assets

```
database/

    er_diagram/

    init/
        001_create_tables.sql
        002_constraints_and_indexes.sql
        003_optional_roles_grants.sql
        ...

    queries/
```

Documentation:

```
docs/section2_database_design.md
```

---

# Section 3 — System Design

The final section contains two architecture designs.

## Design 1 — Secure Database Access

A Role-Based Access Control (RBAC) strategy is proposed for the PostgreSQL database.

Three business roles are modelled:

- Logistics
- Analytics
- Sales

The design applies the Principle of Least Privilege, ensuring each team receives only the permissions required for its responsibilities.

The documentation also discusses:

- Authentication
- Authorization
- Database roles
- Views for analytics
- Auditing
- Operational security

---

## Design 2 — Cloud Image Processing Platform

An AWS architecture is proposed for an image processing platform supporting:

- API-based uploads
- Kafka ingestion
- Image processing
- Metadata storage
- Business Intelligence
- Seven-day archival policy
- Monitoring
- High availability
- Scalability
- Security

The architecture makes use of services including:

- Amazon S3
- ECS Fargate
- Amazon MSK
- API Gateway
- CloudFront
- Route53
- Cognito
- RDS
- Glue
- Athena
- QuickSight
- CloudWatch
- CloudTrail
- IAM
- AWS Config
- WAF
- Shield

Documentation:

```
docs/section3_system_design.md
```

---

# Testing

The ETL pipeline includes both unit and integration tests.

Current test coverage includes:

- Helper functions
- Transformations
- Validators
- End-to-end pipeline execution

Run the test suite with:

```bash
pytest
```

---

# Technologies Used

- Python 3.12
- pandas
- pytest
- PostgreSQL 17
- Docker Compose
- Bash
- Cron
- AWS Architecture (Design)

---

# Design Principles

Throughout the assessment, the solutions were designed with the following engineering principles:

- Separation of concerns
- Modular pipeline design
- Reproducible batch processing
- Traceability of processed datasets
- Third Normal Form (3NF)
- Principle of Least Privilege
- Scalability
- Maintainability
- High availability
- Cloud-native architecture
- Security by design
