import pandas as pd
import matplotlib.pyplot as plt



messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                "Widget A", " Widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200",
              "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
             "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
    "region": ["North", "South", "north", "East", "South",
               "West", "east", "North", "South", "West"],
})

df = pd.DataFrame(messy)
print("=== Raw Data ===")
print(df)
print(f"Total Records {len(df)}")


# Standardize Product and Region
df["product"] = df["product"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()

# Handle Missing/Invalid Values
df = df.dropna(subset=['product'])

# Convert types
df["date"] = pd.to_datetime(df["date"])
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df = df[df["sales"]>0]

# Drop Duplicates
# ======NOTE=======
# I had some questions about this one. Did you mean for Widget B to be a duplicate and mistyped the date
# or are the two entries for Widget B unique to see who would catch it? I wrote two filters & ran it with each in testing.
# You can comment & uncomment the correct one for this assignment.

# This will remove Widget B  200  2025-01-03  South
df = df.drop_duplicates(subset=['product','sales','region'],keep='first')

# This leaves Widget B  200  2025-01-03  South
# df = df.drop_duplicates(subset=['product','sales','region','date'],keep='first')

print("=== Cleaned Data ===")
print(df)
print(f"Total Records {len(df)}")

totalSales_by_product = df.groupby('product')['sales'].sum()

totalSales_by_date = df.groupby('date')['sales'].sum()

totalSales_by_region = df.groupby('region')['sales'].sum()

plt.title("Total sales by product")
plt.xlabel("PRODUCT")
totalSales_by_product.plot(kind='bar')
plt.ylabel("SALES")
plt.xticks(rotation=0)
plt.show()

df["sales"].plot(kind='hist', bins=8, edgecolor='black')
plt.title("Distribution of Sales")
plt.xlabel("SALES")
plt.ylabel("Number of sales")
plt.xticks(rotation=0)
plt.show()

totalSales_by_date.plot(kind='pie')
plt.title("Total sales by date")
plt.xlabel("DATE")
plt.ylabel("SALES")
plt.xticks(rotation=0)
plt.show()

totalSales_by_date.plot(kind='line')
plt.title("Total sales by date")
plt.xlabel("SALES")
plt.ylabel("DATE")
plt.xticks(rotation=0)
plt.show()

totalSales_by_region.plot(kind='hist', bins=8, edgecolor='black')
plt.title("Distribution of Sales by Region")
plt.xlabel("REGION")
plt.ylabel("SALES")
plt.xticks(rotation=0)
plt.show()








