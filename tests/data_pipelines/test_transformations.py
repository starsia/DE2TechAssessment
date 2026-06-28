import sys
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src" / "data_pipelines"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

sys.path.insert(0, str(ROOT / "src"))


from data_pipelines.operations.transformations import (
    create_above18,
    create_membership_id_columns,
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

def test_create_above18_adds_column():
    '''
    Tests the transformation function create_above18.
    '''

    df = load_rows("test_above18.csv")

    result = create_above18(df)

    assert "above_18" in result.columns

    expected = [False, True, True, True, True, False]

    assert result["above_18"].tolist() == expected
    # assert result.loc[0, "above_18"] is True
