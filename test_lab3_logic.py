import pytest
import pandas as pd
from lab3_logic import calculate_fare_by_sex

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Sex": ["male", "female", "male", "female", "male"],
        "Fare": [10, 20, 30, 40, 50]
    })

def test_min_fare(sample_df):
    result = calculate_fare_by_sex(sample_df, "min")
    assert result["male"] == 10
    assert result["female"] == 20

def test_max_fare(sample_df):
    result = calculate_fare_by_sex(sample_df, "max")
    assert result["male"] == 50
    assert result["female"] == 40

def test_avg_fare(sample_df):
    result = calculate_fare_by_sex(sample_df, "avg")
    assert result["male"] == pytest.approx(30.0)
    assert result["female"] == pytest.approx(30.0)

def test_invalid_func_raises(sample_df):
    with pytest.raises(ValueError):
        calculate_fare_by_sex(sample_df, "median")

def test_missing_columns_raises():
    df = pd.DataFrame({"Name": ["A", "B"], "Fare": [10, 20]})
    with pytest.raises(ValueError):
        calculate_fare_by_sex(df, "min")

# python -m pytest -v