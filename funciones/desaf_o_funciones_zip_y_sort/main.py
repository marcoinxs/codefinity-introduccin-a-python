# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = zip(products, prices, quantities_sold)

sorted_products = sorted(combined_list)
#print(sorted_products)

for item1, item2, item3 in sorted_products:
    print(f"Product: {item1}, Price: {item2}, Quantity Sold: {item3}")
