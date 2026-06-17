from pathlib import Path
import os

cwd = os.getcwd()
spark_rel_path = ".venv_pyspark/Scripts"
spark_path_full = Path(cwd) / spark_rel_path

os.environ["SPARK_HOME"] = str(spark_path_full)

print(cwd)
print(spark_path_full)

spark_home = os.environ.get("SPARK_HOME")

print(spark_home)
