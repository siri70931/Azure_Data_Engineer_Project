import dlt

@dlt.table
def dimartist_stg():
    df = spark.readStream.table("catalog_azure.silver.dimartist")
    return df

dlt.create_streaming_table(name="dimartist")

dlt.create_auto_cdc_flow(
    source="dimartist_stg",
    target="dimartist",
    keys=["artist_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2,
    track_history_column_list= None,
    name=None,
    once=False
)

