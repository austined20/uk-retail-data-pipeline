import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
 
    # Remove exact duplicates
    before_duplicate = df.shape[0]
    logger.info("Removing duplicate rows")
    df = df.drop_duplicates()
    after_duplicate = df.shape[0]
    logger.info(f"Removed {before_duplicate-after_duplicate} duplicate rows")
    
    # Remove rows with null CustomerID
    before_custid = df.shape[0]
    logger.info("Dropping rows with null CustomerID")
    df = df.dropna(subset= ['CustomerID'])
    after_custid = df.shape[0]
    logger.info(f"Removed {before_custid-after_custid} rows with null CustomerID")

    # Remove cancelled invoices
    before_cancelled = df.shape[0]
    logger.info("Removing cancelled invoice row")
    df = df[~df["InvoiceNo"].astype(str).str.startswith('C')]
    after_cancelled = df.shape[0]
    logger.info(f"Removed {before_cancelled-after_cancelled} rows with cancelled invoices")

    # Remove negative or zero quantities
    before_neg = df.shape[0]
    logger.info("Removing rows with negative or zero quantities")
    df = df[df["Quantity"] > 0]
    after_neg = df.shape[0]
    logger.info(f"Removed {before_neg-after_neg} rows with negative or zero quantities")

    return df