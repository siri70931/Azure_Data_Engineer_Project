import dlt

expectations = {
    "rule_1": "user_id IS NOT NULL"
}

@dlt.table
@dlt.expect_all_or_drop(expectations)  # The error is due to type checking, but Databricks DLT expects SQL expressions as strings, so this is valid in practice.
def dimuser_stg():
    df = spark.readStream.table("catalog_azure.silver.dimuser")
    return df

dlt.create_streaming_table(name="dimuser")

dlt.create_auto_cdc_flow(
    source="dimuser_stg",
    target="dimuser",
    keys=["user_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_column_list=None,
    name=None,
    once=False
)