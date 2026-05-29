import pandas as pd
import os

def load_data(filepath):
    """Loads the raw CSV data into a pandas DataFrame."""
    print(f"Loading data from: {filepath}")
    return pd.read_csv(filepath)

def clean_missing_values(df):
    """Fills missing values in categorical columns to preserve sensor data."""
    print("Checking for missing data...")
    print(df.isnull().sum())
    
    print("\nApplying data transformations...")
    df['irrigation_type'] = df['irrigation_type'].fillna('Unknown')
    df['crop_disease_status'] = df['crop_disease_status'].fillna('Unknown')
    
    print("Verification: Missing data after cleaning:")
    print(df.isnull().sum())
    return df

def main():
    # 1. Setup paths so the script knows where the data folder is
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    
    raw_data_path = os.path.join(project_root, 'data', 'raw', 'Smart_Farming_Crop_Yield_2024.csv')
    processed_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_farm_data.csv')

    # 2. Execute the ETL Pipeline
    df = load_data(raw_data_path)
    clean_df = clean_missing_values(df)
    
    # 3. Save the clean data to the processed folder
    clean_df.to_csv(processed_data_path, index=False)
    print(f"\nSuccess! Clean data saved to: {processed_data_path}")

# This tells Python to run the main() function when you execute the script
if __name__ == "__main__":
    main()