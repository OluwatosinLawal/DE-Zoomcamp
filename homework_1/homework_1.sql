--Answes to questions 3-6

--Checking samplea o the green taxi trips data
SELECT *
FROM green_taxi_trips
LIMIT 10;


--checking samples of the zone data
SELECT *
FROM zones
LIMIT 10;

--No of trips with a distance of less than or equalto a mile in Nov 2025
SELECT COUNT(*)
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
	AND lpep_pickup_datetime < '2025-12-01'
	AND trip_distance <= 1.0;

--Pickup day with the longest trip distance less than 100 miles
SELECT lpep_pickup_datetime AS pick_up_day,
		MAX (trip_distance)
FROM green_taxi_trips
WHERE trip_distance < 100
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;


--Pick up zone with the largest total amount on Nov 18 2025
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


--Drop of zone with the largest tip in Nov 2025, for passengers in East Harlem North Zone
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