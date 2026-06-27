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

# def test_format_birthday_normalizes_dates_to_yyyymmdd():
#     rows = load_rows("test_success.csv")

#     result = format_birthday(rows)

#     assert(result[1][3] == "20220405")

# def test_remove_missing_name_filters_blank_names():
#     rows = load_rows("test_missing_name.csv")

#     result = remove_missing_name(rows)

#     assert(True)


# def test_create_above18_derives_age_flag():
#     rows = load_rows("test_success.csv")

#     result = create_above18(rows)

#     assert(True)


# def test_create_membership_id_uses_last_name_and_birthdate_hash():
#     rows = load_rows("test_success.csv")

#     result = create_membership_id(rows)

#     assert(True)

