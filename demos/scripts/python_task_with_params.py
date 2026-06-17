import sys

"""
When Databricks Job runs task as a Python script, any parameters need to be passed as a list of strings.
This is a simple example of how to parse the arguments and use them in your code.
"""

print("Arguments passed to the task:", sys.argv)

# Accessing task parameters
job_id = sys.argv[1]
task_name = sys.argv[2]
print(f"Job ID: {job_id}, Task Name: {task_name}")
