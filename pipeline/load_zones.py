import pandas as pd
from sqlalchemy import create_engine

# Download the zones data
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"
print(f"Downloading {url}...")
df = pd.read_csv(url)

# Connect to the database (running on localhost:5432)
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Upload to postgres
print("Inserting data into table 'zones'...")
df.to_sql(name='zones', con=engine, if_exists='replace')
print("Success! Zones table created.")