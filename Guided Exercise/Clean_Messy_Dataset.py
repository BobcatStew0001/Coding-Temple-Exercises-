import pandas as pd
import matplotlib.pyplot as plt

messy_data = {
    "name": ["Alice", "Bob", "Charlie", "  Diana  ", "Eve", "Bob", "Frank", None, "Grace", "Henry"],
    "department": ["Engineering", "marketing", "ENGINEERING", "Sales", "engineering",
                   "marketing", "Sales", None, "Engineering", "sales"],
    "salary": ["95000", "72000", "110000", "68000", "88000",
               "72000", "75000", "82000", "-5000", "78000"],
    "start_date": ["2020-03-15", "2022-01-10", "2018-07-22", "2024-06-01", "2021-11-30",
                   "2022-01-10", "2023-03-15", "2020-08-01", "not a date", "2023-09-15"],
    "email": ["alice@co.com", "bob@co.com", "charlie@co.com", "diana@co.com", "eve@co.com",
              "bob@co.com", "frank@co.com", "unknown@co.com", "grace@co.com", "henry@co.com"],
}

df = pd.DataFrame(messy_data)
print("=== Raw Data ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# Fix Whitespace in Names
df["name"] = df["name"].str.strip()

# Standardize Dept Names
df["department"] = df["department"].str.strip().str.title()

# Convert Salary to Numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Convert Dates
df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")

# Remove Duplicates (Bob appears twice)
df = df.drop_duplicates(subset=["email"], keep="first")

# Handle Missing Values
df = df.dropna(subset=['name'])
df['department'] = df['department'].fillna('Unknown')

# Fix invalid values
df.loc[df['salary'] < 0, "salary"] = pd.NA

print("=====Clean Data=====")
print(df)