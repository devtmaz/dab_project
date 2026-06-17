"""
This script demonstrates how to programatically connect to remote Databricks Cluster
using databricks-connect package.
"""

from databricks.connect import DatabricksSession

spark = (
    DatabricksSession.builder
    # .serverless() # Configure session to use Serverless compute.
    # Alternatively, we can add `serverless_compute_id=auto` inside databricks config.
    .getOrCreate()
)

spark.sql("SHOW SCHEMAS").show()
