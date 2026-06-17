# Test setup

This directory contains unit tests defined for `dab_project`.

**conftest.py** file - contains basic configuration required to run unit tests on both Databricks (using `databricks-connect` package) and local Spark session (using `pyspark` package)

## Test Coverage

Test Coverage refers to amount of code covered by unit tests. Coverage reports can validate our workspace and return the coverage percent per each module.

To get coverage report we need to install 2 packages:
- pytest
- pytest-cov

### Run coverage report for /src directory:

```pwsh
pytest --cov=src --cov-report=term
```

Flag `--cov-report=term` means output coverage report to terminal/command line.


### Exclusions from coverage report

To exclude modules or directories from coverage report we need to create `.coveragerc` file.