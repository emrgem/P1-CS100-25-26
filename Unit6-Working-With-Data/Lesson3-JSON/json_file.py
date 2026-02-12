"""Unit 6 - Lesson 3: Working with JSON"""
# =============================================================================
# 🎯 ACTIVITY 1: Read and Analyze Customer Data
# =============================================================================
# Load customer_data.json and find the highest-spending customer
#
# Expected output:
# Top customer: TechStart Inc
# Total spent: $72,000

# YOUR CODE HERE:
import json
# Load the JSON file
with open("customer_data.json", "r") as file:
    customers = json.load(file)
    print(type(customers)) # List (has dictionaries)
    print(type(customers[0]["total_spent"]))
#Find the highest spender
highest_spender = customers[0]
# print(highest_spender)
for customer in customers:
    if customer["total_spent"] > highest_spender['total_spent']:
        highest_spender = customer

# Display the results
print(f"Top Customer: {highest_spender['name']}")
print(f"Top Customer: ${highest_spender['total_spent']:,}")

# =============================================================================
# 🎯 ACTIVITY 2: Create Product Catalog
# =============================================================================
# Create a product catalog and save it as JSON
#
# Products to include:
# - Wireless Mouse ($29.99, Electronics)
# - USB Cable ($12.99, Accessories)
# - Laptop Stand ($45.00, Furniture)

products = [
    {"id": "P001", "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": "P002", "name": "USB Cable", "price": 12.99, "category": "Accessories"},
    {"id": "P003", "name": "Laptop Stand", "price": 45.00, "category": "Furniture"}
]

# YOUR CODE HERE:
# 1. Write products to "catalog.json" with indent=4
with open("catalog.json", "w") as file:
    json.dump(products, file, indent=4)
print("✅ Catalog created!")

# 2. Read it back and print all product names
with open("catalog.json", "r") as file:
    loaded_products = json.load(file)
print("\nProducts in catalog:")
for product in loaded_products:
    print(f" - {product['name']}")



