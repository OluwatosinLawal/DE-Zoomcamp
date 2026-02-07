-- 1. Create an "External Table" (Points to your GCS files without copying data)
-- NOTE: Update the bucket name 'nyc-tl-data' to YOUR bucket name (e.g. zoomcamp-tosin-2026)
CREATE OR REPLACE EXTERNAL TABLE `zoomcamp.external_yellow_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://zoomcamp-tosin-2026/yellow_tripdata_2019-*.csv', 'gs://zoomcamp-tosin-2026/yellow_tripdata_2020-*.csv']
);

-- 2. Create a "Partitioned Table" (Organizes data by Date)
CREATE OR REPLACE TABLE `zoomcamp.yellow_tripdata_partitioned`
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM `zoomcamp.external_yellow_tripdata`;

-- 3. Create a "Partitioned & Clustered Table" (Organizes by Date AND sorts by VendorID)
CREATE OR REPLACE TABLE `zoomcamp.yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `zoomcamp.external_yellow_tripdata`;