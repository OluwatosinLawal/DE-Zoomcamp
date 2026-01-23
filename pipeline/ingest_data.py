#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[8]:


# Read a sample of the data
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = prefix + 'yellow_tripdata_2021-01.csv.gz'

# Display first rows
display(df.head())

# Check data types
print(df.dtypes)

# Check data shape
print(df.shape)


# In[9]:


# Specify the types to fix the DtypeWarning
# Define data types
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

# Create the iterator WITHOUT the 100 row limit
df_iter = pd.read_csv(
    url,
    iterator=True,
    chunksize=100000,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[6]:


from sqlalchemy import create_engine

# Create Database Connection
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Connect
engine.connect()
print("Connected!")


# In[10]:


from tqdm.auto import tqdm

# Get the first chunk
first_chunk = next(df_iter)

# Create table (replace if exists)
first_chunk.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
print("Table created")

# Insert first chunk
first_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
print("Inserted first chunk:", len(first_chunk))

# Loop over the rest with progress bar
for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    # print("Inserted chunk:", len(df_chunk)) # Optional: verify length


# In[ ]:




