# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for elementos in range(5):
    weekday = weekdays[elementos]
    promotion = daily_promotions[elementos]
    print(f"{weekday}: Promotion on {promotion}")


