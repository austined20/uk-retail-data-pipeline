import pandas as pd
import os
import logging
from config import PROCESSED_DATA_PATH, DB_PATH, TABLE_NAME
import sqlite3

logger = logging.getLogger(__name__)

def save_to_csv(df: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH,index=False)
    logger.info(f"Data successfully saved to {PROCESSED_DATA_PATH}")

def save_to_sqlite(df: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(DB_PATH),exist_ok=True)
    
    logger.info(f"Loading data into SQLite table: {TABLE_NAME}")
    
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

    logger.info(f"Data successfully loaded into SQLite database: {DB_PATH}")

def load_data(df: pd.DataFrame) -> None:
    logger.info("Starting load step")
    save_to_csv(df)
    save_to_sqlite(df)
    logger.info("Load step completed successfully")