from __future__ import annotations
from .helpers import generate_membership_id, normalize_date, split_name
from .validators import validate_above18
import pandas as pd

REFERENCE_DATE = pd.Timestamp("2022-01-01")

# ---------- DataFrame transformations ----------

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
        .apply(validate_above18)
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

def split_name_columns(df):
    df = df.copy()

    df[["first_name", "last_name"]] = (
        df["name"]
        .apply(split_name)
        .apply(pd.Series)
    )

    return df