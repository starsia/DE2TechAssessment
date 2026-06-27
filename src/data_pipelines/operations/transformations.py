from __future__ import annotations
from .helpers import normalize_date
from .validators import is_above18
import hashlib
import pandas as pd

REFERENCE_DATE = pd.Timestamp("2022-01-01")


# ---------- Helper functions ----------


def generate_membership_id(last_name: str, birthday: str) -> str:
    """
    Generate membership ID:

        <last_name>_<first 5 chars of SHA256(YYYYMMDD)>
    """

    digest = hashlib.sha256(
        birthday.encode("utf-8")
    ).hexdigest()[:5]

    return f"{last_name}_{digest}"


# ---------- DataFrame transformations ----------

def split_name(df):
    df = df.copy()

    names = df["name"].str.split(" ", n=1, expand=True)

    df["first_name"] = names[0]
    df["last_name"] = names[1]

    return df


def format_birthday(df):
    df = df.copy()

    df["date_of_birth"] = (
        df["date_of_birth"]
        .apply(normalize_date)
    )

    return df


def remove_missing_name(df):
    return df.dropna(subset=["name"])


def create_above18(df):
    df = df.copy()

    df["above_18"] = (
        df["date_of_birth"]
        .apply(is_above18)
    )

    return df


def create_membership_id(df):
    df = df.copy()

    df["membership_id"] = df.apply(
        lambda row: generate_membership_id(
            row["last_name"],
            row["date_of_birth"],
        ),
        axis=1,
    )

    return df