import sys

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
catalog = sys.argv[1]


spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.00_landing")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.01_bronze")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.02_silver")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.03_gold")

spark.sql(
    f"CREATE VOLUME IF NOT EXISTS {catalog}.00_landing.source_citibike_data"
)
