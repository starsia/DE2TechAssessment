from __future__ import annotations
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from data_pipelines.operations.helpers import normalize_date, split_name

def test_normalize_date():
    assert normalize_date("1986/01/10") == "19860110"
    assert normalize_date("1974-09-10") == "19740910"
    assert normalize_date("02/27/1974") == "19740227"

def test_split_name():
    assert split_name("John Doe") == ("John", "Doe")
    assert split_name("Mr. Scott Martinez") == ("Mr. Scott", "Martinez")
    assert split_name("Madonna") == ("Madonna", "")