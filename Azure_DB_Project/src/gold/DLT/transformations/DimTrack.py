import dlt

@dlt.table
def dimtrack_stg():
    df = spark.readStream.table("catalog_azure.silver.dimtrack")
    return df

dlt.create_streaming_table(name="dimtrack")

dlt.create_auto_cdc_flow(
    source="dimtrack_stg",
    target="dimtrack",
    keys=["track_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_column_list= None,
    name=None,
    once=False
)

