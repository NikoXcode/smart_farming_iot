import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Load the secret credentials from the .env file
load_dotenv()
db_url = os.getenv("DATABASE_URL")

# SQLAlchemy requires 'postgresql://' instead of 'postgres://' for newer versions
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# 2. Locate the clean data
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
clean_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_farm_data.csv')

def upload_to_cloud():
    print("Loading clean data from local CSV...")
    df = pd.read_csv(clean_data_path)
    
    print("Opening secure connection to Aiven Cloud Database...")
    engine = create_engine(db_url)
    
    print("Uploading data (this might take a few seconds)...")
    # 'to_sql' automatically creates the table and uploads the data
    df.to_sql('farm_sensor_data', engine, if_exists='replace', index=False)
    
    print(f"Success! {len(df)} rows securely loaded into the 'farm_sensor_data' table.")

if __name__ == "__main__":
    upload_to_cloud()