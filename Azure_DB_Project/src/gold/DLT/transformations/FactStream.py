import dlt

@dlt.table
def factstream_stg():
    df = spark.readStream.table("catalog_azure.silver.factstream")
    return df

dlt.create_streaming_table(name="factstream")

dlt.create_auto_cdc_flow(
    source="factstream_stg",
    target="factstream",
    keys=["user_id"],
    sequence_by="stream_timestamp",
    stored_as_scd_type=2,
    track_history_column_list= None,
    name=None,
    once=False
)

