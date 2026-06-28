## Problem statement

Apply some transformations to the raw CSV files.

### Assumptions

I made direct decisions on how to handle some edge cases which were not explicit:

- I decided that individuals above 18 years old include those who are 18 from the reference date provided in the assignment. This is because the assignment did not specify whether to include or exclude those who are exactly 18 years old, and I believe it is reasonable to include them.
- How to handle specific names such as "Mr. William Dixon"? Since we are not opinionated on dropping specific parts of names, the split between first and last name will be done on the last space encountered. This will get us Mr William as the first name and Dixon as the last name.

### Project structure

We want to ensure clear separation of concerns in the codebase. The following structure is proposed:

- pipeline.py orchestrates the workflow but contains no business logic.
- validators.py contains only validation rules that return boolean masks or predicates.
- helpers.py contains utility functions that are not specific to any transformation or validation.
- transformations.py contains only deterministic data transformation functions.
- reader.py and writer.py handle I/O.
- Unit tests found in tests/data_pipelines verify the helpers, transformations, and validators independently, while a single integration test exercises the full pipeline on a representative batch. It is noted that the integration test will likely need to be updated as the pipeline evolves, but it is important to have a test that verifies the end-to-end functionality of the pipeline.

To summarise, the business rules lives in validators.py, while every column manipulation lives in transformations.py, which makes the project easier to maintain and aligns well with the separation of concerns.

### Pipeline architecture

The pipeline.py script orchestrates the workflow of the data pipeline. It reads the raw CSV files, applies the necessary transformations and validations, and writes the processed data to the output files. The script is designed to be modular, allowing for easy addition or modification of transformations and validations as needed.

### Data sources

We have two CSV files in data/raw. The extraction pipeline should enter the data/incoming folder and read the CSV files. The pipeline will then apply the necessary transformations and validations to the data, and write the processed data to the data/processed folder. They will be output into the pipeline folder, split into sucessful and unsuccessful.

### Scheduling (cron)

We will use cron to schedule the pipeline. The pipeline will be scheduled to run every hour. The cron job will execute the pipeline.py script, which will orchestrate the workflow and call the necessary functions from the other modules.

### How to run

We can run the pipeline by executing the following command in the terminal:

```bash
python pipeline.py
```

### Testing and validation

We will need a way to validate each transformation is working correctly. For this, we will write unit tests for each transformation and validator function. We will also write an integration test that runs the entire pipeline on a sample dataset and checks that the output matches the expected results.
Here since the pipeline is scheduled to run hourly, we can run the tests by executing the following command in the terminal:

```bash
pytest tests/data-pipelines/test_pipeline.py
```

### Design decisions

In the past I've built data pipelines using Airflow using official Docker images, but for this project, I will use cron to schedule the pipeline. The reason is that the pipeline is relatively simple and does not require complex scheduling or dependency management. Cron is lightweight and easy to set up, making it a suitable choice for this project.

There was some debate about whether to create a package for the pipeline or not. I decided to create a package because it makes testing easier and allows us to update pipelines in different places if we want to make changes to the pipeline.

The constant reference date was lifted into a constants folder to make it easier to update the reference date in the future. This is a good practice as it allows for easy maintenance and updates to the codebase.

### Future improvements
