# Function
def apply_discount(prices):
    prices_copy = prices.copy()
    valor = 0
    for index in range(len(prices_copy)):
        #print(prices_copy[item])
        #valor = prices_copy[price]
        #rounded = f"{valor:.2f}"
        if prices_copy[index] > 2.00:
            #print(prices_copy[item] * 0.9)
            valor = prices_copy[index] * 0.90
            #rounded = f"{valor:.2f}"
            prices_copy[index] = valor
        
        #prices_copy[price] = rounded
    
    return prices_copy
        
# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")
