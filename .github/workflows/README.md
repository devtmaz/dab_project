# GitHub Workflows

This directory contains GitHub Actions workflows for continuous integration and continuous deployment (CI/CD) of the dab_project.

## Workflows Overview

### CI Workflow (ci-workflow.yml)

**Purpose:** Validates code quality and runs unit tests on every pull request.

**Trigger:** Automatically runs when a pull request is opened or updated against the `main` branch.

**Steps:**
1. Checks out the code
2. Sets up Python 3.11
3. Installs PySpark and testing dependencies
4. Runs unit tests with code coverage using pytest
5. Generates HTML coverage report
6. Uploads coverage report as an artifact

**Artifacts:** HTML coverage report (available for download in the workflow run)

---

### CD Workflow (cd-workflow.yml)

**Purpose:** Automatically deploys the project to Databricks workspaces (TEST and PROD environments).

**Trigger:** Automatically runs when code is pushed to the `main` branch.

**Steps:**

#### Deploy to TEST
1. Checks out the code
2. Sets up Python 3.11
3. Installs Databricks CLI
4. Installs build dependencies (setuptools, wheel)
5. Configures Databricks credentials using service principal secrets
6. Deploys bundle to TEST environment using `databricks bundle deploy --target test`

#### Deploy to PROD
1. Runs only after TEST deployment succeeds (dependency)
2. Follows the same steps as TEST deployment
3. Deploys bundle to PROD environment using `databricks bundle deploy --target prod`

**Environment Protection:** Both TEST and PROD deployments use GitHub Environments for credential management and approval workflows.

---

## Required Secrets

For CD workflows to function, configure the following secrets in your GitHub repository settings:

- `SP_CLIENT_ID`: Service Principal Client ID for Databricks authentication
- `SP_CLIENT_SECRET`: Service Principal Client Secret for Databricks authentication

## Workspace Configuration

Update the Databricks workspace URLs in the CD workflow file:
- Line 32: TEST workspace URL
- Line 65: PROD workspace URL

----------
[Go back to main README](../../README.md)