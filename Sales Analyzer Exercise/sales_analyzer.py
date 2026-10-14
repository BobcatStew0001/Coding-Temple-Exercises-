import csv

#Reads sales_data.csv using DictReader

sales_data = []

with open("sales_data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales_data.append(row)

# print(sales_data) making sure that it will read the file correctly.

#Step 2 Calculates: Total Revenue, Total Quantity, Revenue per product, total quantity sold
#per product, the day with the highest total revenue

total_revenue = 0
total_quantity = 0
revenue_by_product = {}
quantity_by_product = {}
revenue_by_date = {}
#I included all calculations into one for loop
for product in sales_data:
    revenue = product["quantity"] * product["price"]
    total_revenue += revenue
    total_quantity += product["quantity"]
#I combined the by products into one if/else
    if product["product"] not in revenue_by_product:
        revenue_by_product[product["product"]] = revenue
        quantity_by_product[product["product"]] = product["quantity"]
#I combined the by date into one if/else
    else:
        revenue_by_product[product["product"]] += revenue
        quantity_by_product[product["product"]] += product["quantity"]

    if product["date"] not in revenue_by_date:
        revenue_by_date[product["date"]] = revenue

    else:
        revenue_by_date[product["date"]] += revenue
    #Used the max() shortcut vs writing out the logic.
highest_revenue_date = max(revenue_by_date, key=revenue_by_date.get)
#Tested to make sure the code ran and returns the correct results
# print(total_quantity)
# print(total_revenue)
# print(revenue_by_product)
# print(quantity_by_product)
# print(revenue_by_date)
# print(highest_revenue_date)


with open("sales_report.txt", "w") as file:
    file.write("=" * 40 + "\n")
    file.write("          Sales Report\n")
    file.write("=" * 40 + "\n")
    file.write(f"Total Revenue: {total_revenue:.2f}\n")
    file.write(f"Total Quantity: {total_quantity}\n")
    file.write('--------------------\n')
    file.write("*** Product Breakdown ***\n")
    for name in revenue_by_product:
        file.write(f"{name}: {revenue_by_product[name]:.2f}\n")
        file.write(f"Quantity: {quantity_by_product[name]}\n")
    file.write('--------------------\n')
    file.write("*** Revenue By Date ***\n")
    for name in revenue_by_date:
        file.write(f"{name}: {revenue_by_date[name]:.2f}\n")
    file.write('--------------------\n')
    file.write("*** Highest Revenue ***\n")
    file.write(f"Highest Revenue: {highest_revenue_date} {revenue_by_date[highest_revenue_date]:.2f}\n")

with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader()
    for name in revenue_by_product:
        writer.writerow({'product': name, 'total_revenue': round(revenue_by_product[name],2), 'total_quantity': quantity_by_product[name]})



