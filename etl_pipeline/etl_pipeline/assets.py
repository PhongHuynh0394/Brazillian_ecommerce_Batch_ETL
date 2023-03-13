from dagster import asset

@asset
def first_asset():
    return "hello world"
