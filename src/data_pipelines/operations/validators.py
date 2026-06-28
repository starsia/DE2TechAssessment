import pandas as pd
import re

from .constants import REFERENCE_DATE
from .helpers import normalize_date

def validate_mobile_no(phone_number: str) -> bool:
    """
    Returns True if phone number is valid:
    - Phone number is exactly 8 digits long
    - Phone number contains only digits
    """
    phone_number = str(phone_number).replace(" ", "")

    return phone_number.isdigit() and len(phone_number) == 8

def validate_email(email: str) -> bool:
    """
    Returns True if email is valid
    """
    EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")

    email = str(email).strip().lower()

    if EMAIL_PATTERN.match(email):
        return True

    return False


def validate_above18(date_of_birth: str) -> bool:
    """
    Returns True if applicant is over 18 as of 1 Jan 2022.
    Accepts any supported date format.
    """

    normalized = normalize_date(date_of_birth)

    birthday = pd.to_datetime(normalized, format="%Y%m%d")

    age = (
        REFERENCE_DATE.year
        - birthday.year
        - (
            (REFERENCE_DATE.month, REFERENCE_DATE.day)
            < (birthday.month, birthday.day)
        )
    )

    return age >= 18

def validate_name(name: str) -> bool:
    """
    Returns True if name is not empty.
    """
    return pd.notna(name) and str(name).strip() != ""