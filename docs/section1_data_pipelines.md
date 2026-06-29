# Section 1: Data Pipeline

## Problem Statement

The objective of this section is to design and implement an hourly ETL pipeline that processes membership applications submitted to an e-commerce platform.

Applications arrive as one or more CSV files every hour and are deposited into a processing directory. The pipeline is responsible for:

- ingesting all incoming datasets
- cleaning and standardising the data
- validating each application against the business rules
- generating membership IDs for successful applicants
- separating successful and unsuccessful applications
- producing consolidated output datasets for downstream consumers

The solution also includes automated scheduling, unit tests, and integration tests to ensure the pipeline behaves correctly as it evolves.

---

# Solution Overview

The pipeline follows a traditional batch ETL architecture.

```
Extract
    ↓
Transform
    ↓
Validate
    ↓
Load
```

Each pipeline execution processes every CSV dropped into the `data/to_process` directory as a single batch. The datasets are consolidated into one DataFrame before business logic is applied.

Applications are then separated into successful and unsuccessful datasets before being written to a timestamped output directory.

```
data/
├── to_process/
│
└── output/
    └── YYYYMMDD_HHMMSS/
        ├── input/
        │   ├── applications_dataset_1.csv
        │   ├── applications_dataset_2.csv
        │   └── ...
        │
        ├── successful.csv
        └── unsuccessful.csv
```

Keeping every execution in its own timestamped directory provides a complete audit trail. Each batch preserves the original input files alongside the processed outputs, allowing downstream engineers to trace every generated record back to its source data.

---

# Repository Structure

The implementation separates orchestration, business logic and I/O into independent modules.

```
src/
└── data_pipelines/
    ├── pipeline.py
    └── operations/
        ├── reader.py
        ├── writer.py
        ├── helpers.py
        ├── transformations.py
        ├── validators.py
        └── constants.py
```

Responsibilities are divided as follows:

| Component            | Responsibility                                           |
| -------------------- | -------------------------------------------------------- |
| `pipeline.py`        | Orchestrates the ETL workflow                            |
| `reader.py`          | Reads and consolidates incoming CSV files                |
| `writer.py`          | Writes processed datasets into timestamped batch folders |
| `transformations.py` | Performs deterministic column transformations            |
| `validators.py`      | Implements business validation rules                     |
| `helpers.py`         | Shared utility functions                                 |
| `constants.py`       | Shared configuration (e.g. reference date)               |

This separation keeps business rules isolated from orchestration and makes each component independently testable.

---

# Transformations

The following transformations are applied to every application.

| Transformation                   | Purpose                                                 |
| -------------------------------- | ------------------------------------------------------- |
| Split name                       | Creates `first_name` and `last_name` columns            |
| Standardise birthday             | Converts all dates into `YYYYMMDD` format               |
| Remove spaces from phone numbers | Normalises phone numbers before validation              |
| Create `above_18`                | Calculates applicant age relative to the reference date |
| Generate membership ID           | Created only for successful applications                |

Applications without a name are treated as unsuccessful, in accordance with the assignment requirements.

---

# Validation Rules

An application is considered successful only if all validation rules pass.

| Validation    | Rule                                                 |
| ------------- | ---------------------------------------------------- |
| Mobile number | Exactly 8 digits                                     |
| Age           | Applicant is at least 18 years old on 1 January 2022 |
| Email         | Valid email format                                   |

Applications failing any validation rule are written to `unsuccessful.csv`.

---

# Scheduling

The pipeline is scheduled using **cron**, which is appropriate for a lightweight hourly batch process.

Supporting scripts are located in:

```
scripts/
├── run_pipeline.sh
├── install_cron.sh
└── remove_cron.sh
```

Install the hourly schedule:

```bash
./scripts/install_cron.sh
```

Remove the schedule:

```bash
./scripts/remove_cron.sh
```

Run the pipeline manually:

```bash
./scripts/run_pipeline.sh
```

---

# Testing

The pipeline is covered by both unit tests and an integration test to verify correctness at multiple levels.

The test suite is organised as follows:

tests/
└── data_pipelines/
├── fixtures/
│ ├── test_above18.csv
│ └── test_shortened_applications_dataset_1.csv
│
├── test_helpers.py
├── test_transformations.py
├── test_validators.py
└── test_pipeline.py

### Unit Tests

Individual components are tested in isolation to ensure each piece of business logic behaves correctly.

| Test file               | Purpose                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| test_helpers.py         | Tests reusable helper functions such as date normalisation and name splitting.                                            |
| test_transformations.py | Tests each DataFrame transformation independently (birthday formatting, membership ID generation, age calculation, etc.). |
| test_validators.py      | Tests all validation rules, including email, mobile number and age validation.                                            |

Testing each transformation independently makes failures easy to diagnose and reduces the likelihood of regressions when business rules change.

### Integration Test

The integration test exercises the complete ETL pipeline using a representative batch of applications.

test_pipeline.py verifies that the pipeline:

- successfully reads an input dataset
- applies all required transformations
- performs all validation rules
- separates successful and unsuccessful applications
- generates membership IDs for successful applicants
- produces the expected output datasets

This provides confidence that all individual components work correctly when composed into the complete pipeline.

### Test Fixtures

The fixtures/ directory contains representative CSV datasets used throughout the tests. These provide deterministic inputs so that transformations and validation logic can be verified against known expected outputs.

### Running the Tests

Execute the complete test suite with:

```
pytest
```

# Processed Outputs

A sample processed batch is included under:

```
samples/
```

Each sample batch contains:

- original input datasets
- consolidated successful applications
- consolidated unsuccessful applications

These outputs demonstrate the expected results produced by the pipeline.

---

# Design Decisions

Several implementation decisions were made where the specification left room for interpretation.

- Applicants exactly 18 years old on **1 January 2022** are considered eligible (`>= 18`).
- Names are split on the final whitespace character so titles (e.g. "Mr. Jeff Baker") remain part of the first name.
- Phone numbers are normalised by removing embedded spaces before validation.
- Email validation follows RFC conventions and is case-insensitive.
- Business logic is separated from orchestration to maximise maintainability and testability.
- Cron was selected over Airflow because the pipeline consists of a single independent hourly batch without workflow dependencies.

---

# Future Improvements

Given additional time, the pipeline could be extended with:

- configurable input/output locations via environment variables
- structured logging instead of console output
- retry handling for failed batches
- data quality reporting and pipeline metrics
- Airflow orchestration for production deployments
- cloud object storage (e.g. Amazon S3) instead of local filesystem storage
- containerisation of the pipeline using Docker
