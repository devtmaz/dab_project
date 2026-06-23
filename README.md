# dab_project

This is a repository created during Udemy course `CI/CD with Databricks Asset Bundles`.

Primary repository URL with Wiki owned by course instructor: https://github.com/pathfinder-analytics-uk/dab_project.

## Table of Contents

- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
  - [Virtual Environment Setup](#virtual-environment-setup)
  - [Java Setup for Local PySpark Development](#java-setup-for-local-pyspark-development)
  - [Unit Tests with Pytest](#unit-tests-with-pytest)
  - [Databricks CLI, Set-Up and Bundle Commands](#databricks-cli-set-up-and-bundle-commands)

## Project structure

```
dab_project/
├── .github/
│   └── workflows/              GitHub Actions CI/CD workflows
├── demos/                      Demo scripts and YAML configurations demonstrating core concepts
├── docs/                       Project documentation (diagrams, data models)
├── src/                        Python source code and utilities
├── resources/                  Resource configurations (jobs, pipelines)
├── tests/                      Unit tests for shared Python code
├── fixtures/                   Test data sets
├── notebooks/                  Notebooks for testing project setup
├── citibike_etl/               ETL workflows and scripts
├── databricks.yml              Databricks Asset Bundle configuration
├── setup.py                    Python packaging configuration for wheel distribution
├── requirements-dbc.txt        Databricks Connect dependencies
├── requirements-pyspark.txt    PySpark dependencies
└── README.md                   Project documentation
```


## Getting started

### Prerequisites

Before you proceed, ensure you have:

- [ ] Completed the Udemy course setup (Databricks Workspaces, Service Principals, GitHub Repository)
- [ ] Updated the `databricks.yml` configuration file with your Workspace URLs and Service Principal details
- [ ] Python 3.11 installed on your system
- [ ] Java Development Kit (JDK) 8, 11, or newer (required for local PySpark development)
- [ ] Databricks CLI installed

### Setup Instructions

Follow the instructions for your platform below to set up local Python environments for Databricks Connect and local PySpark development.

### Virtual Environment Setup

#### macOS / Linux

1. **Create and activate the Databricks Connect environment (using Python 3.11)**
   ```bash
   # at the project root
   python3.11 -m venv .venv_dbc
   source .venv_dbc/bin/activate
   ```
2. **Install Databricks Connect dependencies**
   ```bash
   pip install -r requirements-dbc.txt
   ```
3. **Verify installation**
   ```bash
   pip list
   deactivate
   ```

4. **Create and activate the local PySpark environment**
   ```bash
   python3.11 -m venv .venv_pyspark
   source .venv_pyspark/bin/activate
   ```
5. **Install PySpark dependencies**
   ```bash
   pip install -r requirements-pyspark.txt
   ```
6. **Verify installation**
   ```bash
   pip list
   deactivate
   ```

#### Windows

1. **Create and activate the Databricks Connect environment (using Python 3.11)**
   ```powershell
   # at the project root
   py -3.11 -m venv .venv_dbc
   .\.venv_dbc\Scripts\activate
   ```
2. **Install Databricks Connect dependencies**
   ```powershell
   pip install -r requirements-dbc.txt
   ```
3. **Verify installation**
   ```powershell
   pip list
   deactivate
   ```

4. **Create and activate the local PySpark environment**
   ```powershell
   py -3.11 -m venv .venv_pyspark
   .\.venv_pyspark\Scripts\Activate.ps1
   ```
5. **Install PySpark dependencies**
   ```powershell
   pip install -r requirements-pyspark.txt
   ```
6. **Verify installation**
   ```powershell
   pip list
   deactivate
   ```

---

### Java Setup for Local PySpark Development

This project uses `pyspark` as its data processing and transformation technology. To develop and test pyspark code on a local environment, you need to install Java Development Kit (JDK).

#### macOS / Linux

1. Download Java JDK 8, 11, or newer from [Oracle Java Download Website](https://www.oracle.com/java/technologies/downloads/). Recommended version is JDK 11.
   ```bash
   # Example: Download and install JDK 11
   # On macOS with Homebrew:
   brew install java11
   ```

2. Set the `JAVA_HOME` environment variable:
   ```bash
   # Find your Java installation path
   /usr/libexec/java_home -v 11
   
   # Add to your shell profile (~/.zprofile, ~/.bash_profile, or ~/.bashrc)
   export JAVA_HOME=$(/usr/libexec/java_home -v 11)
   ```

3. Verify Java installation:
   ```bash
   java --version
   ```

#### Windows

1. Download Java JDK 8, 11, or newer from [Oracle Java Download Website](https://www.oracle.com/java/technologies/downloads/). Recommended version is JDK 11.
2. Add new `JAVA_HOME` system environment variable with the path to the folder with Java installation:

   **Windows**

   | Variable | Value |
   |----------|-------|
   | `JAVA_HOME` | `C:\Program Files\Java\jdk-11.0.31` |
   | `Path` (add entry) | `C:\Program Files\Java\jdk-11.0.31\bin` |


3. Verify Java installation:
   ```pwsh
   java --version
   ```
   Output should look like this:
   ```
   java 11.0.31 2026-04-21 LTS
   Java(TM) SE Runtime Environment 18.9 (build 11.0.31+9-LTS-165)
   Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.31+9-LTS-165, mixed mode)
   ```

---

### Unit Tests with Pytest

This project uses the `Pytest` framework for unit tests.

#### macOS / Linux

1. Activate the virtual environment with installed `pyspark` and `pytest` packages:
   ```bash
   source .venv_pyspark/bin/activate
   ```

2. Run unit tests:
   ```bash
   pytest tests
   ```

#### Windows

1. Activate the virtual environment with installed `pyspark` and `pytest` packages:
   ```powershell
   .\.venv_pyspark\Scripts\Activate.ps1
   ```

2. Run unit tests:
   ```powershell
   pytest tests
   ```

#### Configure Unit Tests in VS Code

Alternatively, you can configure unit tests in Visual Studio Code:

1. Install the `Python extension for Visual Studio Code` from VS Code Extensions.
2. Navigate to the **Testing** tab in VS Code.
3. Configure unit tests:
   - Select `Pytest` as the testing framework
   - Select `tests` folder as the unit tests folder
4. Unit tests should now be visible in the Testing window.



### Databricks CLI, Set-Up and Bundle Commands

1. Install the Databricks CLI
   ```bash
   curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
   ```
   or alternatively on a MacOS if you need admin override
   ```bash
   sudo curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh
   ```

2. Authenticate to your Databricks workspace, if you have not done so already:
    ```bash
    databricks configure
    ```

3. To deploy a development copy of this project, type:
    ```bash
    databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)

    This deploys everything that's defined for this project.
    For example, the default template would deploy a job called
    `[dev yourname] dab_project_job` to your workspace.
    You can find that job by opening your workspace and clicking on **Workflows**.

4. Similarly, to deploy a production copy, type:
   ```bash
   databricks bundle deploy --target prod
   ```

   Note that the default job from the template has a schedule that runs every day
   (defined in resources/dab_project.job.yml). The schedule
   is paused when deploying in development mode (see
   https://docs.databricks.com/dev-tools/bundles/deployment-modes.html).

5. To run a job or pipeline, use the "run" command:
   ```bash
   databricks bundle run
   ```

6. Optionally, install developer tools such as the Databricks extension for Visual Studio Code from
   https://docs.databricks.com/dev-tools/vscode-ext.html.

7. For documentation on the Databricks asset bundles format used
   for this project, and for CI/CD configuration, see
   https://docs.databricks.com/dev-tools/bundles/index.html.


## CI-CD Setup

Refer to [Worflows README](.github/workflows/README.md) for more details about CI-CD setup for this project
