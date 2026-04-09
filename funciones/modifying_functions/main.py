def apply_discount(price, discount=0.05):
    app_dis = price * (1 - discount)
    return app_dis

def  apply_tax(price, tax=0.07):
    app_tax = price * (1 + tax)
    return app_tax

def calculate_total(price, discount=0.05, tax=0.07):
    app_dis = apply_discount(price, discount)
    total_price_default = apply_tax(app_dis, tax)
    return total_price_default 

ct = calculate_total(120)
print(f"Total cost with default discount and tax: ${ct:.2f}")

ctd = calculate_total(100, 0.10, 0.08)
print(f"Total cost with custom discount and tax: ${ctd:.2f}")
