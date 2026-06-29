from __future__ import annotations
from .helpers import generate_membership_id, normalize_date, split_name, remove_gap_in_mobile_no
from .validators import validate_above18
import pandas as pd

REFERENCE_DATE = pd.Timestamp("2022-01-01")

# ---------- DataFrame transformations ----------

def format_birthday(df):
    """
    Apply helper function called normalize_date to the date_of_birth column
    Standardizes different date formats
    """
    df = df.copy()

    df["date_of_birth"] = (
        df["date_of_birth"]
        .apply(normalize_date)
    )

    return df


def create_above18(df):
    """
    Apply helper function called validate_above_18 to the date_of_birth column
    Note that this should only be applied after format_birthday function is called to avoid odd formats. 
    """
    df = df.copy()

    df["above_18"] = (
        df["date_of_birth"]
        .apply(validate_above18)
    )

    return df


def create_membership_id_columns(df):
    """
    Apply helper function called generate_membership_id using last_name and date_of_birth columns
    Note that this should only be applied after format_birthday function is called to avoid odd formats. 
    """
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
    """
    Apply helper function called split_name using name column
    """
    df = df.copy()

    df[["first_name", "last_name"]] = (
        df["name"]
        .apply(split_name)
        .apply(pd.Series)
    )

    return df


def remove_gap_in_mobile_no_column(df):
    """
    Apply remove_gap_in_mobile_no to dataframe
    """

    df = df.copy()

    df["mobile_no"] = df["mobile_no"].apply(remove_gap_in_mobile_no)

    return df