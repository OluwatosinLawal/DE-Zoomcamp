import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

# Define the data types (from our previous steps)
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

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    
    print(f"Connecting to postgresql://{pg_user}:***@{pg_host}:{pg_port}/{pg_db}...")
    
    # Create database connection
    connection_string = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    engine = create_engine(connection_string)

    # Data URL
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    
    print(f"Downloading data from {url}...")

    # Create iterator
    df_iter = pd.read_csv(
        url, 
        iterator=True, 
        chunksize=100000, 
        dtype=dtype, 
        parse_dates=parse_dates
    )

    # Get first chunk to create table
    first_chunk = next(df_iter)

    print(f"Creating table '{target_table}'...")
    first_chunk.head(0).to_sql(name=target_table, con=engine, if_exists='replace')
    
    print("Inserting first chunk...")
    first_chunk.to_sql(name=target_table, con=engine, if_exists='append')

    print("Inserting remaining chunks...")
    for chunk in tqdm(df_iter):
        chunk.to_sql(name=target_table, con=engine, if_exists='append')

    print("Finished! Data ingestion complete.")

if __name__ == '__main__':
    run()