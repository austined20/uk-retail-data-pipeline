import logger
from ingest import ingest_data
from clean import clean_data
from transform import transform_data
from load import load_data
from config import RAW_DATA_PATH
from validate import validate_data
import logging

logger = logging.getLogger(__name__)

def main():

    try:
        logger.info("Pipeline started")
        df = ingest_data(RAW_DATA_PATH)
        validate_data(df)
        df = clean_data(df)
        df = transform_data(df)
        load_data(df)
        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()