# UK Retail Data Pipeline

## Overview

This project implements an end-to-end **data pipeline** on a real-world UK retail dataset.  
The pipeline ingests raw data, validates and cleans it, applies transformations, and loads the processed data into both **CSV** and a **SQLite database** for analysis.

---

## Goal

Build a production-style ETL pipeline using Python and SQL.

## Architecture

```
Raw CSV
↓
Ingest
↓
Validate
↓
Clean
↓
Transform
↓
Load → CSV + SQLite
```

---

## Tech Stack

- Python
- Pandas
- SQLite
- Logging
- Git & GitHub

---

## Project Structure

```
uk-retail-data-pipeline/
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── db/
│
├── logs/
│
├── src/
│ ├── ingest.py
│ ├── validate.py
│ ├── clean.py
│ ├── transform.py
│ ├── load.py
│ ├── config.py
│ ├── logger.py
│ └── query_checks.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Pipeline Details

### Ingest
- Reads raw CSV data
- Validates file existence and non-empty input

### Validate
- Column/schema validation
- Null value threshold checks
- Negative quantity validation (excluding cancellations)
- Duplicate row checks
- Date format validation

### Clean
- Removed duplicate rows
- Dropped null `CustomerID`
- Removed cancelled invoices (`InvoiceNo` starting with 'C')
- Removed invalid negative quantities

### Transform
- Converted `InvoiceDate` to datetime
- Created `TotalPrice` column
- Extracted `Year` and `Month`
- Standardized `StockCode`
- Converted `CustomerID` to integer

### Load
- Saved cleaned data to CSV
- Loaded data into SQLite database (`retail.db`, table: `retail_data`)

---

## Sample SQL Analysis

### Total Records
392,732 rows after cleaning

### Distinct Customers
4,339 customers

### Top Countries
- United Kingdom (~89% of transactions)
- Germany, France, EIRE follow

### Monthly Revenue Trend
- Peak revenue in **November 2011 (~1.15M)**
- Strong growth observed from September to November
- Lower December due to partial data

---

## Setup & Usage

### 1. Clone Repository

```
git clone <your-repo-link>
cd uk-retail-data-pipeline
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Dataset
Place the dataset file in:

data/raw/online_retail.csv


### 5. Run Pipeline

```bash
python main.py
```

### 6. Run SQL Queries

```
python src/query_checks.py
```

---

## Key Learnings

- Built a modular ETL pipeline using Python
- Implemented logging and data validation layers
- Handled real-world data issues (returns, missing values)
- Loaded and queried data using SQLite

---

## Future Improvements

- Load data into PostgreSQL
- Add workflow orchestration (e.g., Airflow)
- Implement automated data quality checks
- Build dashboards on top of processed data

---

## Dataset

UK Online Retail Dataset (Kaggle)

---
