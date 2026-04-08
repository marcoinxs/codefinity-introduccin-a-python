# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started\n")

for articulos in inventory:
    #print(f"Processing {articulos}: {inventory[articulos][3]}")
    print(f"Processing {articulos}")
    current_stock = inventory[articulos][0]
    minimum_stock =inventory[articulos][1]
    restock_quantity = inventory[articulos][2]
    on_sale = inventory[articulos][3]
    while current_stock < minimum_stock:
        #print(f"Processing {articulos}: {current_stock}")
        current_stock += restock_quantity
        inventory[articulos][0] = current_stock
        if current_stock > discount_threshold:
            inventory[articulos][3] = True

#print(inventory)
print("\nProcessing completed")