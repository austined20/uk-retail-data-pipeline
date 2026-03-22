import sqlite3
from config import DB_PATH, TABLE_NAME

def run_query(query: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

    for row in rows:
        print(row)

def main() -> None:
    queries = {
        "total_rows" : f"SELECT COUNT(*) FROM {TABLE_NAME}",

        "distinct_customers" : f"SELECT COUNT(DISTINCT CustomerID) FROM {TABLE_NAME}",

        "top_countries" : f"""SELECT Country, COUNT(*) AS total_orders FROM {TABLE_NAME} GROUP BY Country
                    ORDER BY total_orders DESC
                    LIMIT 10""",

        "top_customers" : f"""SELECT CustomerID, ROUND(SUM(TotalPrice), 2) AS revenue FROM {TABLE_NAME} GROUP BY CustomerID ORDER BY revenue DESC
                        LIMIT 10""",

        "monthly_revenue" : f"""SELECT Year, Month, ROUND(SUM(TotalPrice), 2) AS monthly_revenue
                        FROM {TABLE_NAME} GROUP BY Year, Month ORDER BY Year, Month"""
    }

    for name, query in queries.items():
        print(f"\n----{name}-----")
        run_query(query)

if __name__ == "__main__":
    main()