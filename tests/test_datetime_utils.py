import pytest
from datetime import datetime

from src.utils.datetime_utils import timestamp_to_date_col


@pytest.fixture(scope="function")
def sample_timestamp_df(spark):
    """Create a sample DataFrame with timestamp data."""
    schema = "id STRING, start_time TIMESTAMP"

    data = [
        ("1", datetime(2024, 1, 15, 10, 30, 0)),
        ("2", datetime(2024, 2, 20, 14, 45, 0)),
        ("3", datetime(2024, 3, 25, 9, 15, 0)),
        ("4", None),
    ]

    return spark.createDataFrame(data, schema=schema)


def test_basic_timestamp_to_date_conversion(spark, sample_timestamp_df):
    """Test that timestamps are correctly converted to dates."""
    result_df = timestamp_to_date_col(
        spark, sample_timestamp_df, "start_time", "ride_date"
    )

    # Check that output column exists and has correct datatype
    assert "ride_date" in result_df.columns
    assert dict(result_df.dtypes)["ride_date"] == "date"

    # Collect and verify results
    rows = result_df.collect()
    assert len(rows) == 4

    # Check that dates are extracted correctly
    assert str(rows[0]["ride_date"]) == "2024-01-15"
    assert str(rows[1]["ride_date"]) == "2024-02-20"
    assert str(rows[2]["ride_date"]) == "2024-03-25"
    assert (
        rows[3]["ride_date"] is None
    )  # null timestamp should result in null date
