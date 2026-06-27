import sys
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src" / "data_pipelines"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

sys.path.insert(0, str(ROOT / "src"))


from data_pipelines.operations.transformations import (
    split_name,
    format_birthday,
    remove_missing_name,
    create_above18,
    create_membership_id,
)

def load_rows(filename):
    return pd.read_csv(FIXTURES / filename)

def test_split_name_adds_first_and_last_name_columns():
    df = load_rows("test_success.csv")

    result = split_name(df)
    print(result)
    assert "first_name" in result.columns
    assert "last_name" in result.columns

    assert result.loc[0, "first_name"] == "John"
    assert result.loc[0, "last_name"] == "Smith"

def test_format_birthday_formats_as_yyyymmdd():
    df = load_rows("test_success.csv")

    result = format_birthday(df)

    assert result.loc[0, "birthday"] == "19980101"

def test_remove_missing_name_removes_rows_without_name():
    df = load_rows("test_missing_name.csv")

    result = remove_missing_name(df)

    assert len(result) == len(df) - 1
    assert result["name"].isna().sum() == 0

def test_create_above18_adds_column():
    df = load_rows("test_success.csv")

    result = create_above18(df)

    assert "above_18" in result.columns
    assert result.loc[0, "above_18"] is True

def test_create_membership_id_adds_column():
    df = load_rows("test_success.csv")

    result = create_membership_id(df)

    assert "membership_id" in result.columns
    # assert result.loc[0, "membership_id"].startswith("Smith_")
