## Data Pipelines Skill

Use this guidance when working on membership application ingestion and transformation.

### Goal

Convert the raw application CSV files into validated outputs for successful and unsuccessful applications.

### Required Checks

- Mobile number must contain exactly 8 digits after removing formatting characters.
- Email must end with `@emailprovider.com` or `@emailprovider.net`.
- Applicant must be older than 18 as of 1 Jan 2022.
- Rows without a usable name must be treated as unsuccessful.

### Transformation Rules

- Split the name into `first_name` and `last_name` using a deterministic rule and document it.
- Normalize the birthday to `YYYYMMDD` before any downstream use.
- Add an `above_18` field derived from the birthday and cutoff date.
- Generate membership IDs for successful rows using `<last_name>_<sha256(birthday)[:5]>`.
- Consolidate outputs into separate successful and unsuccessful datasets.

### Test-First Expectations

- Write tests for each validation rule before implementing the transformation logic.
- Add edge-case tests for malformed dates, whitespace in mobile numbers, and names with titles or suffixes.
- Verify that successful and unsuccessful counts are stable on the sample datasets.
- Testing will be done using pytest.

### Validation Artifacts

- A pipeline function or module that can be run against the sample CSV files.
- A test suite that proves the transformation contract.
- A markdown note describing scheduling and file-handling assumptions.
