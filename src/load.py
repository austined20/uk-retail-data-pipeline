import pandas as pd
import os
import logging
from config import PROCESSED_DATA_PATH, DB_PATH, TABLE_NAME
import sqlite3
import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

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
 
def save_to_postgres(df: pd.DataFrame) -> None:
    logger.info("Loading data into PostgreSQL")

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS retail_data (
            InvoiceNo TEXT,
            StockCode TEXT,
            Description TEXT,
            Quantity INTEGER,
            InvoiceDate TIMESTAMP,
            UnitPrice FLOAT,
            CustomerID INTEGER,
            Country TEXT,
            TotalPrice FLOAT,
            Year INTEGER,
            Month INTEGER
        );
    """)

    cursor.execute("TRUNCATE TABLE retail_data;")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO retail_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    logger.info("Data successfully loaded into PostgreSQL")

def load_data(df: pd.DataFrame) -> None:
    logger.info("Starting load step")
    save_to_csv(df)
    save_to_sqlite(df)
    save_to_postgres(df)
    logger.info("Load step completed successfully")