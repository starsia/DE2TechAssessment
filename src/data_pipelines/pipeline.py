from datetime import datetime
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
    remove_gap_in_mobile_no_column,
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
    working = remove_gap_in_mobile_no_column(working)

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

    timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    if df.empty:
        print(f"No datasets found at {timestamp}")
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