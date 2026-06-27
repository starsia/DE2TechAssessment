from __future__ import annotations

import sys
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src" / "data-pipelines"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

sys.path.insert(0, str(ROOT / "src"))

from data_pipelines.operations.validators import validate

def load_rows(filename):
    return pd.read_csv(FIXTURES / filename)


def test_validate_accepts_row_batch_with_expected_contract():
    rows = load_rows("test_success.csv")

    result = validate(rows)

    assert(False)

def test_validate_rejects_invalid_rows():
    rows = load_rows("test_invalid.csv")

    result = validate(rows)

    assert(False)
