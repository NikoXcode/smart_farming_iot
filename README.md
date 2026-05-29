# Smart Farming IoT Data Pipeline

## Overview
This repository contains an end-to-end Extract, Transform, Load (ETL) pipeline for agricultural IoT data. It processes raw sensor readings (temperature, soil moisture, rainfall) and prepares the dataset for downstream Machine Learning and predictive analytics.

## Project Structure
* `data/raw/`: Contains the raw, unedited IoT sensor logs (CSV).
* `data/processed/`: Contains the cleaned data ready for model training.
* `src/data_processing.py`: The core Python script that automates the data cleaning and transformation process.
* `notebooks/`: Contains Jupyter notebooks for initial exploratory data analysis.

## How to Run
1. Ensure your raw data is placed in the `data/raw/` directory.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Execute the processing script: `python src/data_processing.py`