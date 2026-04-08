# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item in inventory:
    discounted_price = inventory[item][2]
    regular_price = inventory[item][1]
    print(f"Articulo: {item} - Inventario: {inventory[item][0]} - Precio: {regular_price} - Descuento: {inventory[item][2]}")
    if inventory[item][0] < 30:
        print(f"{item} need restocking.")

    if inventory[item][0] > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")

    if 30 <= inventory[item][0] <= 100:
        print(f"{item} should be sold at the regular price of {regular_price}.")
