from pathlib import Path
import sys
import pandas as pd

from data_pipelines.operations.reader import read_all
from data_pipelines.operations.writer import write
from data_pipelines.operations.transformations import split_name_columns
from data_pipelines.operations.transformations import (
    split_name_columns,
    format_birthday,
    create_above18,
    create_membership_id_columns,
)
from data_pipelines.operations.validators import (
    validate_mobile_no,
    validate_email,
    validate_above18,
    validate_name,
)

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "data"
INCOMING = Path(__file__).resolve().parent / "incoming"

sys.path.insert(0, str(ROOT / "src"))

def load_rows(filename):
    return pd.read_csv(INCOMING / filename)


def run_pipeline(df):
    df = df.copy()

    # -------------------------
    # Transformations
    # -------------------------

    df = split_name_columns(df)
    df = format_birthday(df)
    df = create_above18(df)

    # -------------------------
    # Validation
    # -------------------------

    valid_mobile = df["mobile_no"].apply(validate_mobile_no)

    valid_email = df["email"].apply(validate_email)

    valid_age = df["date_of_birth"].apply(validate_above18)

    valid_name = df["name"].apply(validate_name)

    valid = (
        valid_mobile
        & valid_email
        & valid_age
    )

    # -------------------------
    # Split datasets
    # -------------------------

    successful = df[valid].copy()
    unsuccessful = df[~valid].copy()

    # Membership IDs only for successful applications
    successful = create_membership_id_columns(successful)

    return successful, unsuccessful

if __name__ == '__main__':
    df = load_rows("test_shortened_applications_dataset.csv")

    df = read_all()

    successful, unsuccessful = run_pipeline(df)

    write(successful, unsuccessful)

    # move incoming/applications_dataset_1.csv into raw/applications_dataset_1.csv