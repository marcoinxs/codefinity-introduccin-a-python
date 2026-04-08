produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

print(groceries)

for section in groceries:
    print(section)
    for item in section:
        print("Item name:", item)
    

