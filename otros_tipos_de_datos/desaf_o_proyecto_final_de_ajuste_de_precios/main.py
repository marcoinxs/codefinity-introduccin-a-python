# Dictionary for a grocery store grocery_inventory 
grocery_inventory  = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

if "Eggs" in grocery_inventory: 
    if grocery_inventory.get("Eggs")[1] > 5:
        print("Eggs are too expensive, reducing the price by $1.")
        grocery_inventory.update({"Eggs":("Dairy", 4.5, 30)})
    else:
        print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

if "Eggs" in grocery_inventory: 
    if grocery_inventory.get("Milk")[2] < 10:
        print("Milk needs to be restocked. Increasing stock by 20 units.")
        grocery_inventory.update({"Milk":("Dairy", 3.50, 28)})
    else:
        print("Milk has sufficient stock.")

print("Updated inventory: ", grocery_inventory)

