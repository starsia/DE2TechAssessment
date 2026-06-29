from data_pipelines.operations.validators import (
    validate_mobile_no,
    validate_email,
    validate_above18
)

def test_mobile_length():
    """
    Mobile number can only be 8 digits. We include starting numbers <8 because it may be other countries.
    """
    assert validate_mobile_no("91234567") is True
    assert validate_mobile_no("1234567") is False
    assert validate_mobile_no("123456789") is False
    assert validate_mobile_no("1234abcd") is False

def test_validate_email():
    """
    Email must be valid as per convention. 
    """
    assert validate_email("john@emailprovider.com")
    assert validate_email("john@emailprovider.net")
    assert validate_email("john@gmail.com")
    assert validate_email("alice@company.org")

    assert not validate_email("not-an-email")
    assert not validate_email("alice@")
    assert not validate_email("@emailprovider.com")

def test_validate_above18():
    """
    Age must be above 18. We calculate this from the reference date. 
    """
    assert validate_above18("2000-01-01") is True
    assert validate_above18("2003-12-31") is True
    assert validate_above18("2004-01-01") is True   # exactly 18
    assert validate_above18("2004-01-02") is False  # one day too young, 17 years, 364 days