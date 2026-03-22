import pandas as pd

def main():
    file_path='data/raw/online_retail.csv'

    df=pd.read_csv(file_path,encoding='unicode_escape')

    print(df.head())

    print("Shape",df.shape)

    print("\nColumns:\n",df.columns)

    print("\nNull Counts:\n",df.isnull().sum())

    print("\nUnique Countries:\n",df["Country"].nunique())
    print("\nCount by Country:\n", df["Country"].value_counts())

    print("\nNegative quantity rows:", len(df[df["Quantity"] < 0]))

    print("\nDuplicate rows:\n", df.duplicated().sum())

    print(df[df["Quantity"] < 0].head())

    print("\nNegative quantity rows with C:",df[df["Quantity"] < 0]["InvoiceNo"].astype(str).str.startswith("C").sum())

    print("\nNull CustomerID with negative quantity:\n",df[(df["CustomerID"].isnull()) & (df["Quantity"] < 0)].shape)

    print(df[df.duplicated()].head())

    print("\nDuplicate count:\n",df.duplicated().sum())

if __name__ == "__main__":
    main()
