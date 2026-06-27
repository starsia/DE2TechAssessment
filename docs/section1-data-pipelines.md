## Problem statement

Apply some transformations to the raw CSV files.

### Assumptions

### Project structure

We want to ensure clear separation of concerns in the codebase. The following structure is proposed:

- pipeline.py orchestrates the workflow but contains no business logic.
- transformations.py contains only deterministic data transformation functions.
- validators.py contains only validation rules that return boolean masks or predicates.
- reader.py and writer.py handle I/O.
  Unit tests verify every transformation and validator independently, while a single integration test exercises the full pipeline on a representative batch.

### Pipeline architecture

### Scheduling (cron)

### How to run

### Testing and validation

We will need a way to validate each transformation is working correctly. For this, we will write unit tests for each transformation and validator function. We will also write an integration test that runs the entire pipeline on a sample dataset and checks that the output matches the expected results.
Here since the pipeline is scheduled to run hourly, we can run the tests by executing the following command in the terminal:

```bash
pytest tests/data-pipelines/test_pipeline.py
```

### Design decisions

In the past I've built data pipelines using Airflow using official Docker images, but for this project, I will use cron to schedule the pipeline. The reason is that the pipeline is relatively simple and does not require complex scheduling or dependency management. Cron is lightweight and easy to set up, making it a suitable choice for this project.

### Future improvements
