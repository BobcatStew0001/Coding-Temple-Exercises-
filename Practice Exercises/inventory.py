











# #Start with a dictionary of at least 4 products. Each product should have a name (key) with a nested dictionary
# # containing price (float) and quantity (int):
# inventory = {
#     "beer": {
#         "price": 14.99,
#         "quantity": 48
#     },
#     "chips": {
#         "price": 2.99,
#         "quantity": 32
#     },
#     "dog food": {
#         "price": 4.99,
#         "quantity": 15
#     },
#     "toilet paper": {
#         "price": 3.99,
#         "quantity": 12
#     },
#     "meat sticks":{
#         "price": 5.99,
#         "quantity": 20
#     },
#     "soda": {
#         "price": 2.99,
#         "quantity": 24
#     },
#     "candy bars": {
#         "price": 1.49,
#         "quantity": 18
#     }
#     }
# # Display the full inventory in a formatted table
# total_value = 0
# print("=" * 50)
# print(f"{'Product':<15}{'Price':>10}{'Quantity':>10}  {'Item-Value':>12}")
# print("=" * 50)
# for name, details in inventory.items():
#     item_value = details["price"] * details["quantity"]
#     total_value += item_value
#     price_text = f"${details['price']:.2f}"
#     item_value_text = f"${item_value:.2f}"
#     print(f"{name.title():<15} {price_text:>10} {details['quantity']:>10}{item_value_text:>12}")
# print("=" * 50)
# # Calculate and display the total value of the inventory (price × quantity for each product, summed)
# total_text = f"${total_value:.2f}"
# print(f"{'Total Inventory Value:':<37}{total_text:>12}")
# print("=" * 50)
# # Let the user look up a product and see its details (using .get() for safety)
# search = input("Enter a product to look up: ").strip().lower() #Used strip and lower throughout to safeguard against crazy n-put
# product = inventory.get(search)
# if product:
#     price_text = f"${product['price']:.2f}"
#     item_value = product["price"] * product["quantity"]
#     item_value_text = f"${item_value:.2f}"
#     print(f"{search.title():<15} {price_text:>10} {product['quantity']:>10}{item_value_text:>12}")
# else:
#     print( f"{search.title()} was not found in the inventory")
# print("=" * 50)
# # Let the user update the quantity of a product (simulating a sale or restock)
# search = input("Enter a product to update: ").strip().lower()
# product = inventory.get(search)
# if product: #I added the nested if statement to prevent overselling
#     change = int(input("Enter amount sold (negative) or restocked (positive): "))
#     if product["quantity"] + change < 0:
#         print(f"Not enough stock. Only {product['quantity']} {search.title()} available.")
#     else:
#         old_quantity = product["quantity"]
#         product["quantity"] += change
#         print(f"{search.title()} quantity updated: {old_quantity} -> {product['quantity']}")
# else:
#     print(f"{search.title()} was not found in the inventory")
# # Use a set to track which products are "low stock" (quantity < 10)
# low_stock = set()
# for name, details in inventory.items():
#     if details["quantity"] < 10:
#         low_stock.add(name)
#
# print("=" * 50)
# if low_stock:
#     print("LOW STOCK ALERT - These products need restocking:")
#     for item in sorted(low_stock):
#         print(f"  - {item.title()} ({inventory[item]['quantity']} left)")
# else:
#     print("All products are well stocked.")
# print("=" * 50)
#
# #I tested it multiple times using variations of Beer, Milk, Dog Food, Meat Sticks with various spacing aNd forMaTTING to
# #make sure it worked and safeguards caught any anomalies.
