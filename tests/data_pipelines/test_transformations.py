import sys
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src" / "data_pipelines"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

sys.path.insert(0, str(ROOT / "src"))


from data_pipelines.operations.transformations import (
    remove_missing_name,
    create_above18,
    create_membership_id,
    split_name_columns,
)

from data_pipelines.operations.helpers import split_name

def load_rows(filename):
    return pd.read_csv(FIXTURES / filename)

def test_split_name_adds_first_and_last_name_columns():
    '''
    Create two new columns called first_name and last_name 
    Using the split_name function on the 'name' column
    '''
    df = load_rows("test_success.csv")

    result = split_name_columns(df)

    assert "first_name" in result.columns
    assert "last_name" in result.columns

    assert result.loc[0, "first_name"] == "William"
    assert result.loc[0, "last_name"] == "Dixon"


def test_remove_missing_name_removes_rows_without_name():
    df = load_rows("test_missing_name.csv")

    result = remove_missing_name(df)

    assert len(result) == len(df) - 1
    assert result["name"].isna().sum() == 0

# def test_create_above18_adds_column():
#     df = load_rows("test_success.csv")

#     result = create_above18(df)

#     assert "above_18" in result.columns
#     assert result.loc[0, "above_18"] is True

# def test_create_membership_id_adds_column():
#     df = load_rows("test_success.csv")

#     result = create_membership_id(df)

#     assert "membership_id" in result.columns
    # assert result.loc[0, "membership_id"].startswith("Smith_")
