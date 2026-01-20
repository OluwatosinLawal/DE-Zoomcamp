import sys
import pandas as pd

#Print the argument passed to the script
print("arguments", sys.argv)

#Capture the first argument as the "day"
day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

#Create a dummy DataFrame
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

#Save it to a parquet file usin the day argument in the filename
df.to_parquet(f"output_day_{sys.argv[1]}.parquet")