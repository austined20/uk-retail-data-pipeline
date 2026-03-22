import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    logger.info("Creating TotalPrice column")
    # Create TotalPrice column
    df["TotalPrice"] = (df["Quantity"] * df["UnitPrice"]).round(2)

    logger.info("Extracting Year and Month")
    # Extract useful time features
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month

    df["CustomerID"] = df["CustomerID"].astype(int)

    df["StockCode"] = df["StockCode"].astype(str).str.strip()

    return df
