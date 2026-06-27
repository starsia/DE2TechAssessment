import pandas as pd

def normalize_date(date_of_birth: str) -> str:
    """
    Convert a birthday to YYYYMMDD.

    Supports:
        yyyy/mm/dd
        yyyy-mm-dd
        dd/mm/yyyy
        mm/dd/yyyy
    """

    return (
        pd.to_datetime(date_of_birth, format="mixed")
        .strftime("%Y%m%d")
    )