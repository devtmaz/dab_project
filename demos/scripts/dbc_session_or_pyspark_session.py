"""
This script demonstrates how to check origin of the SparkSession.
"""

try:
    from databricks.connect import DatabricksSession

    spark = DatabricksSession.builder.getOrCreate()

    print("Using DatabricksSession")
except ImportError:
    try:
        from pyspark.sql import SparkSession

        spark = SparkSession.builder.getOrCreate()
        print("Using SparkSession")

    except ImportError:
        print(
            "Error: Neither DatabricksSession nor SparkSession could be imported."
        )
