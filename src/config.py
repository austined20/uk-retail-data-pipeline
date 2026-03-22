import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "online_retail.csv")

PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_retail.csv")

LOG_FILE = os.path.join(BASE_DIR, "logs", "pipeline.log")

DB_PATH = os.path.join(BASE_DIR, "data", "db", "retail.db")

TABLE_NAME = "retail_data"