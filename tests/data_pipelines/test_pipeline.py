from data_pipelines.pipeline import run_pipeline
import sys
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src" / "data_pipelines"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

sys.path.insert(0, str(ROOT / "src"))

def load_rows(filename):
    return pd.read_csv(FIXTURES / filename)

def test_pipeline_shortened_dataset():
    """
    Test the function pipeline in pipeline.py. Uses a shortened csv file based on sample csv file provided. 
    """
    df = load_rows("test_shortened_applications_dataset_1.csv")

    successful, unsuccessful = run_pipeline(df)
    print(successful)
    print(unsuccessful)

    # one successful application
    assert len(successful) == 1

    row = successful.iloc[0]

    assert row["first_name"] == "William"
    assert row["last_name"] == "Dixon"
    assert row["date_of_birth"] == "19860110"
    assert row["above_18"] == True

    assert row["membership_id"].startswith("Dixon_")
    assert len(row["membership_id"].split("_")[1]) == 5


    # everyone else failed
    assert len(unsuccessful) == 15