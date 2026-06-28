from datetime import datetime
from pathlib import Path
import shutil

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]

OUTPUT = ROOT / "data" / "output"


def write(
    successful_df: pd.DataFrame,
    unsuccessful_df: pd.DataFrame,
    input_files: list[Path],
) -> Path:
    """
    Creates a batch output directory.

    output/
        YYYYMMDD_HHMMSS/
            input/
            successful.csv
            unsuccessful.csv
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    batch = OUTPUT / timestamp

    input_dir = batch / "input"

    input_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    successful_df.to_csv(
        batch / "successful.csv",
        index=False,
    )

    unsuccessful_df.to_csv(
        batch / "unsuccessful.csv",
        index=False,
    )

    # Make transactions atomic
    copied = []

    for file in input_files:
        destination = input_dir / file.name
        shutil.copy2(file, destination)
        copied.append(file)

    for file in copied:
        file.unlink()

    return batch