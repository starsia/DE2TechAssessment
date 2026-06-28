from pathlib import Path
import sys

import pandas as pd

from data_pipelines.operations.reader import read_all
from data_pipelines.operations.writer import write

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
)


def run_pipeline(df) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = df.copy()

    # ---------------------------------------
    # Missing names
    # ---------------------------------------

    missing_name = df["name"].isna() | (
        df["name"].astype(str).str.strip() == ""
    )

    unsuccessful_missing = df[missing_name].copy()

    working = df[~missing_name].copy()

    # ---------------------------------------
    # Transformations
    # ---------------------------------------

    working = split_name_columns(working)
    working = format_birthday(working)
    working = create_above18(working)

    # ---------------------------------------
    # Validation
    # ---------------------------------------

    valid = (
        working["mobile_no"].apply(validate_mobile_no)
        & working["email"].apply(validate_email)
        & working["date_of_birth"].apply(validate_above18)
    )

    successful = working[valid].copy()

    unsuccessful = working[~valid].copy()

    unsuccessful = pd.concat(
        [unsuccessful_missing, unsuccessful],
        ignore_index=True,
    )

    successful = create_membership_id_columns(successful)

    return successful, unsuccessful


if __name__ == "__main__":

    df, files = read_all()

    if df.empty:
        print("No datasets found.")
        sys.exit(0)

    successful, unsuccessful = run_pipeline(df)

    batch = write(
        successful,
        unsuccessful,
        files,
    )

    print(f"Processed {len(files)} file(s)")
    print(f"Successful : {len(successful)}")
    print(f"Unsuccessful : {len(unsuccessful)}")
    print(f"Batch written to {batch}")