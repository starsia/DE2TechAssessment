from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]

TO_PROCESS = ROOT / "data" / "to_process"


def read_all() -> tuple[pd.DataFrame, list[Path]]:
    """
    Reads every CSV currently waiting to be processed.

    Returns
    -------
    tuple
        (
            consolidated dataframe,
            list of source csv paths
        )
    """

    files = sorted(TO_PROCESS.glob("*.csv"))

    if not files:
        return pd.DataFrame(), []

    dfs = [
        pd.read_csv(file)
        for file in files
    ]

    df = pd.concat(
        dfs,
        ignore_index=True,
    )

    return df, files