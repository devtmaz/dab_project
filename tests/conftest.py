import sys
import os
import pytest

os.environ["PYSPARK_PYTHON"] = (
    sys.executable
)  # required to set python interpreter for PySpark

# Run the tests from the root directory
sys.path.append(os.getcwd())


@pytest.fixture(scope="session")
def spark():
    """Create a SparkSession for testing.

    Tries to create Databricks Session to execute tests on Databricks.
    If it fails, tries to create local SparkSession.

    Returns
    -------
    spark:
        DatabricksSession or SparkSession.

    Raises
    ------
    ImportError:
        If neither DatabricksSession nor SparkSession could be
        established.
    """
    try:
        from databricks.connect import DatabricksSession

        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession

            spark = SparkSession.builder.master("local[1]").getOrCreate()

        except ImportError:
            raise ImportError(
                "Error: Cannot establish either DatabricksSession or "
                "SparkSession for tests."
            )

    return spark
