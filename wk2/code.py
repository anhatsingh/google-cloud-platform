from google.cloud import storage
from typing import Any

def get_file_from_bucket(bucket_name: str, file_name: str) -> Any:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    return blob.open("r")

bucket = "ibd-week-1"
file = "wk1-input.txt"

with get_file_from_bucket(bucket, file) as f:
    lines = len(f.readlines())
    print(f'File "{file}" in the bucket "{bucket}" contains {lines} number of lines')
