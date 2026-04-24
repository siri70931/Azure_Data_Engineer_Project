This file contains datasets which are used for copying the data from sql table to storage group containers.

AzureSqlTable1 - This dataset is used to copy the data from SQL table to bronze folder in storage group contianers.

Json_Dynamic_DS - It is used to et cdc json file from container and it defined as dynamic, so that we can reuse it by using parameters.

Parquet_dynamic_ds - This dataset is used as destination thing, to store the result in silver container in parquet format, it is also defined dynamically.
