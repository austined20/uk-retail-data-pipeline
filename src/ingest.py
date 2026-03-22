import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def ingest_data(file_path: str) -> pd.DataFrame:

    if not os.path.exists(file_path):
        logger.error("Data file does not exist.")
        raise FileNotFoundError(f"{file_path} not found.")

    if os.path.getsize(file_path) == 0:
        logger.error("File is empty.")
        raise ValueError("Input file is empty.")

    try:
        df=pd.read_csv(file_path, encoding="unicode_escape")
        logger.info(f"Successfully loaded data with shape: {df.shape}")
        return df
    
    except Exception as e:
        logger.exception("Failed to read CSV file.")
        raise e
