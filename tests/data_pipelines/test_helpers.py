from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from data_pipelines.operations.helpers import normalize_date, split_name

def test_normalize_date():
    """
    Ensures that parsing of dates are correct given various formats:
    yyyy/mm/dd
    yyyy-mm-dd
    mm/dd/yyyy
    """
    assert normalize_date("1986/01/10") == "19860110"
    assert normalize_date("1974-09-10") == "19740910"
    assert normalize_date("02/27/1974") == "19740227"

def test_split_name():
    """
    Ensures that splitting of names into first and last names are correct:
    - William Dixon will be split into William (first name) and Dixon (last name)
    - Mr. Patrick Star will be split into Mr. Patrick (first name) and Star (last name)
    """
    assert split_name("John Doe") == ("John", "Doe")
    assert split_name("Mr. Scott Martinez") == ("Mr. Scott", "Martinez")
    assert split_name("Madonna") == ("Madonna", "")

