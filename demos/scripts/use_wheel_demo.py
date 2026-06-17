"""
This script was created to confirm that project packages for dab_project
were correctly installed in a wheel task of Databricks job.
"""

from citibike.citibike_utils import get_trip_duration_mins

print("""
    If you see this message, it means the wheel was installed successfully 
    and we can import the function from the citibike_utils module without any issues.
""")
