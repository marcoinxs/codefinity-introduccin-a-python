grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce") ,
}

print(grocery_inventory)

# Get the count of Bread
bread_details = grocery_inventory.get("Bread")
print("Details of Bread: ", bread_details)

grocery_inventory.update({"Cookies":(143, "Dairy")})
print(f"Inventory after adding Cookies: {grocery_inventory}.")

removed_item = grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}.")