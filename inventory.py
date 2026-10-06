
#Start with a dictionary of at least 4 products. Each product should have a name (key) with a nested dictionary
# containing price (float) and quantity (int):

# Instructions:
# Display the full inventory in a formatted table
# Calculate and display the total value of the inventory (price × quantity for each product, summed)
# Let the user look up a product and see its details (using .get() for safety)
# Let the user update the quantity of a product (simulating a sale or restock)
# Use a set to track which products are "low stock" (quantity < 10)

# Expected output should include:
# A formatted inventory display
# Total inventory value
# A lookup result
# A low-stock alert listing products that need restocking

inventory = {
    "beer": {
        "price": 14.99,
        "quantity": 48
    },
    "chips": {
        "price": 2.99,
        "quantity": 32
    },
    "dog food": {
        "price": 4.99,
        "quantity": 15
    },
    }
