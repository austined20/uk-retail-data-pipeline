import pandas as pd
import logging

logger = logging.getLogger(__name__)

def validate_data(df: pd.DataFrame):

    #column validation
    expected_columns = ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
    if set(expected_columns) != set(df.columns):
        logger.error("Column mismatch")
        raise ValueError(f"Expected columns {expected_columns}, but got {list(df.columns)}")
    
    #null check
    null_perc = (df["CustomerID"].isnull().sum() / df.shape[0]) * 100
    if null_perc > 30:
        logger.error("Too many null CustomerID values")
        raise ValueError(f"{null_perc:.2f}% null CustomerIDs")
    
    #negative quantity
    neg_count = ((df["Quantity"] <= 0) & (~df["InvoiceNo"].str.startswith("C"))).sum()
    if neg_count > 20:
        logger.warning("Too many negative quantities")
    
    #duplicates
    duplicate_count = round((df.duplicated().sum()),0) 
    if duplicate_count > 20:
        logger.warning("Too many duplicate rows")
    
    #date validation
    invalid_dates = pd.to_datetime(df["InvoiceDate"],errors="coerce").isnull().sum() 
    if invalid_dates > 20:
        logger.error("Invalid date values found")
        raise ValueError(f"{invalid_dates} invalid date values")
    
    logger.info("Data Validation passed")
    
