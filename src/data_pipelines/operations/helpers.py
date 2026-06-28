import pandas as pd
import hashlib

# These helper functions take in an input and transform it using some application logic.
# They can be applied in transformation steps using .apply()

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


def generate_membership_id(last_name: str, birthday: str) -> str:
    """
    Generate membership ID:

        <last_name>_<first 5 chars of SHA256(YYYYMMDD)>
    """

    digest = hashlib.sha256(
        birthday.encode("utf-8")
    ).hexdigest()[:5]

    return f"{last_name}_{digest}"

def split_name(name: str) -> tuple[str, str]:
    parts = str(name).strip().rsplit(" ", maxsplit=1)

    if len(parts) == 1:
        return parts[0], ""

    return parts[0], parts[1]