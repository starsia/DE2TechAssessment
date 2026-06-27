import pandas as pd

''' 
We have to apply some transformations to the data. They are split up to ensure scalability and testability
Applications are batched into a varying number of datasets and dropped into a folder on an hourly basis. You are required to set up a pipeline to ingest, clean, perform validity checks, and create membership IDs for successful applications. An application is successful if:

- Application mobile number is 8 digits
- Applicant is over 18 years old as of 1 Jan 2022
- Applicant has a valid email (email ends with @emailprovider.com or @emailprovider.net)

You are required to format datasets in the following manner:

- Split name into first_name and last_name
- Format birthday field into YYYYMMDD
- Remove any rows which do not have a name field (treat this as unsuccessful applications)
- Create a new field named above_18 based on the applicant's birthday
- Membership IDs for successful applications should be the user's last name, followed by a SHA256 hash of the applicant's birthday, truncated to first 5 digits of hash (i.e <last_name>_<hash(YYYYMMDD)>)
'''

def split_name(df):
    return pd.DataFrame([])

def format_birthday(df):
    return pd.DataFrame([])

def remove_missing_name(df):
    return pd.DataFrame([])


def create_above18(df):
    return pd.DataFrame([])


def create_membership_id(df):
    return pd.DataFrame([])
