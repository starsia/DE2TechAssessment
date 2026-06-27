import pandas as pd

def validate_mobile_no(phone_number: str) -> bool:
    toTest = str(phone_number).replace(" ", "")
    if not toTest.isdigit():
        return False
    if len(toTest) != 8:
        return False
    return True


def validate_email(email: str) -> bool:
    return False

def validate_above18(age: str) -> bool:
    return False