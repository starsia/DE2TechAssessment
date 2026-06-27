from data_pipelines.operations.reader import read_all
from operations import (
    split_name,
    format_birthday,
    remove_missing_name,
    create_above18,
    create_membership_id,
)
from data_pipelines.operations.validators import validate
from data_pipelines.operations.writer import write
import pandas as pd

def run_pipeline(*args, **kwargs):
    print("hello world")
    df = read_all()

    df = split_name(df)
    df = format_birthday(df)
    df = remove_missing_name(df)
    df = create_above18(df)

    valid = validate(df)

    successful = df[valid]
    unsuccessful = df[~valid]

    successful = create_membership_id(successful)

    write(successful)
    write(unsuccessful)

    return None

if __name__ == '__main__':
    run_pipeline()