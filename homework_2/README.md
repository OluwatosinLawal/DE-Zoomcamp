# [**Module 2 Homework**](https://github.com/OluwatosinLawal/DE-Zoomcamp/tree/main/homework_2)
This file contains the solutions to the module 2 homework that covers Testra workflow orchestration with Postgres and Bigquery.

## **Question 1**
Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)

****

**Answer: 134.5 MiB**

## **Question 2**
* What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?**

****

**green_tripdata_2020-04.csv**

## **Question 3**
**How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?**

```sql
SELECT count(*) 
FROM `zoomcamp.yellow_tripdata` 
WHERE filename LIKE '%2020%';
```

**Answer: 24,648,499**

## **Question 4**
** How many rows are there for the Green Taxi data for all CSV files in the year 2020?**

```sql
SELECT count(*) 
FROM `zoomcamp.green_tripdata` 
WHERE filename LIKE '%2020%';
```

**Answer: 1,734,051**

## **Question 5**
**How many rows are there for the Yellow Taxi data for the March 2021 CSV file?**

```sql
SELECT count(*) 
FROM `zoomcamp.yellow_tripdata` 
WHERE filename LIKE '%2021-03%';
```

**Answer: 1,925,152**

## **Question 6**
**How would you configure the timezone to New York in a Schedule trigger?**

**Answer: Add a timezone property set to America/New_York in the Schedule trigger configuration**



### **Learning in public links**
[LinkedIn](https://www.linkedin.com/posts/oluwatosin-lawal-70105810b_dataengineering-dezoomcamp-kestra-activity-7424202513387565056-wPP_?utm_source=share&utm_medium=member_desktop&rcm=ACoAABuX_vEBrMwbp394uco22GvbJi1UsrI2R7o)





