from pprint import pprint

from unicodedata import category

products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]


in_stock_products = [status for status in products if status["in_stock"] == True]
print("---Step 1---")
print(in_stock_products)

def discounted_price (product):
    """Return a copy of the product with the original and discounted price. Does not modify the original dict."""
    return{**product,"discounted_price": round(product["price"] - product["price"] * .10, 2)}

results = [discounted_price(product) for product in products]

pprint(results)
print("---Step 3---")
# Extra Practice I wrote it twice

# result = [product for product in products if product["category"] == "electronics" and product["price"] < 200]

result = list(filter(lambda product: product["category"] == "electronics" and product["price"] < 200, products))
pprint(result)

print("---Step 4---")
sorted_products = sorted(products, key=lambda product: product["price"])
pprint(sorted_products)

print("---Step 5---")
in_stock_total = round(sum(product["price"] for product in in_stock_products), 2)
print(in_stock_total)

print("---Step 6---")
product_categories = {product["category"] for product in products}
by_category = {category: [product for product in products if product["category"] == category] for category in product_categories}
pprint(by_category)


