# [**Module 1 Homework**](https://github.com/OluwatosinLawal/DE-Zoomcamp/tree/main/homework_1)
This file contains the solutions to the module 1 homework that covers Docker, SQL and Terraform.

## **Question 1**
What's the version of pip in the python:3.13 image?

**This downloads the image and starts it**
**Command**
```bash
docker run -it --entrypoint bash python:3.13
```
Then run thisto check the version
```bash
pip –version
```

**Output**
```bash
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

**Answer: 25.3**

## **Question 2**
**Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?**

**Based on the YAML file, Docker network (docker-compose), containers talk to each other using their Service Names which is (services:db) in line 2 o my docker file. The internal port name also shows (5432)**

**My Docker Compose Configuration:**

```yaml
services:
  postgres:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data"
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
```

**Answer: db:5432**

## **Question 3**
**For the trips in November 2025, how many trips had a trip_distance of less than or equal to 1 mile?**

```sql
SELECT COUNT(*)
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
	AND lpep_pickup_datetime < '2025-12-01'
	AND trip_distance <= 1.0;
```

**Answer: 8,007**

## **Question 4**
**Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles.**

```sql
SELECT lpep_pickup_datetime AS pick_up_day,
		MAX (trip_distance)
FROM green_taxi_trips
WHERE trip_distance < 100
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```
**Answer: 2025-11-14**

## **Question 5**
**Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?**

```sql
SELECT z."Zone",
		SUM (g.total_amount) AS Amt
FROM green_taxi_trips AS g
JOIN zones AS z
	ON g."PULocationID" = Z."LocationID"
WHERE g.lpep_pickup_datetime >= '2025-11-18'
	AND g.lpep_pickup_datetime < '2025-11-19'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

**Answer: East Harlem North**

## **Question 6**
**Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?**

```sql
SELECT dz."Zone",
		MAX (g.tip_amount) AS tips
FROM green_taxi_trips AS g
JOIN zones AS pz
	ON g."PULocationID" = pz."LocationID"
JOIN Zones AS dz
	ON g."DOLocationID" = dz."LocationID"
WHERE g.lpep_dropoff_datetime >= '2025-11-01'
	AND g.lpep_dropoff_datetime < '2025-12-01'
	AND pz."Zone" = 'East Harlem North'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

**Answer: Yorkville West**

## **Question 7**
**Question 7. Which of the following sequences describes the Terraform workflow for: 1) Downloading plugins and setting up backend, 2) Generating and executing changes, 3) Removing all resources?**

**Answer: terraform init, terraform apply -auto-approve, terraform destroy**

### **Learning in public links**
[LinkedIn](https://www.linkedin.com/posts/oluwatosin-lawal-70105810b_dataengineering-vscode-datatalksclub-activity-7421629918863577088-Wgv9?utm_source=share&utm_medium=member_desktop&rcm=ACoAABuX_vEBrMwbp394uco22GvbJi1UsrI2R7o)


