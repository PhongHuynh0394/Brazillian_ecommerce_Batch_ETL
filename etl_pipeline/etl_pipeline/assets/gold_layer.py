from dagster import asset, Output, AssetIn
import pandas as pd

@asset(
    io_manager_key="minio_io_manager",
    ins={
        "dim_products": AssetIn(
            key_prefix=["silver", "ecom"]
        ),
        "fact_sales": AssetIn(
            key_prefix=["silver", "ecom"]
        )
    },
    group_name="Gold_layer",
    key_prefix=["gold", "ecom"],
    compute_kind="Minio"
)
def sales_values_by_category(dim_products: pd.DataFrame, fact_sales: pd.DataFrame) -> Output[pd.DataFrame]:
    di = dim_products
    fa = fact_sales
    # daily_sales_product
    pass