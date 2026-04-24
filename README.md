# Azure_Data_Engineer_Project

This project demonstrates an end-to-end data engineering pipeline built on Azure using the Medallion Architecture (Bronze → Silver → Gold).

The pipeline leverages streaming ingestion, incremental processing, and Slowly Changing Dimension (SCD Type 2) to create historical, analytics-ready datasets.

Used pipeline to ingest data from bronze container to silver container using CDC for incremental loading data, and created alerts using logic apps incase of failure of pipeline via Email mentioning the pipeline details.

# Tech Stack - 
Azure Data Lake Storage Gen2 – Data storage
Azure Data Factory – Pipeline orchestration
Azure Databricks – Data processing
Delta Live Tables (DLT) – Pipeline automation & data quality
Delta Lake – ACID storage layer
Apache Spark – Distributed processing

# Bronze Layer (Raw Data) - 
Raw data ingested into ADLS Gen2
Stored in Parquet format
No transformations applied
Serves as the single source of truth
df = spark.read.format("parquet") \
    .load("abfss://bronze@<storage-account>.dfs.core.windows.net/table_name")

# Silver Layer (Cleaned & Structured Data) - 
Incremental ingestion using Auto Loader (cloudFiles)
Data cleansing and schema enforcement applied
df_silver = spark.readStream.format("cloudFiles") \ .option("cloudFiles.format", "parquet") \                                                                                    .option("cloudFiles.schemaLocation",                                                                                                 "abfss://silver@<storage-account>/checkpoint") \                                                                     .load("abfss://bronze@<storageaccount>/table_name")

# Gold Layer (DLT + SCD Type 2) - 
The Gold layer is implemented using Delta Live Tables (DLT) and applies SCD Type 2 logic to maintain historical records.

import dlt

@dlt.table
def staging_table():
    return spark.readStream.table("catalog_azure.silver.table_name")

dlt.create_streaming_table(name="table_name")

dlt.create_auto_cdc_flow(
    source="staging_table",
    target="table_name",
    keys=["col"],
    sequence_by="updated_at",
    stored_as_scd_type=2
)
