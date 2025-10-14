def calculate_order(drink_type, size, add_ons):
    prices = {
        "coffee": {"small": 3, "medium": 4, "large": 5},
        "tea": {"small": 2, "medium": 3, "large": 4},
        "juice": {"small": 4, "medium": 5, "large": 6}
    }

    base_price = prices.get(drink_type, {}).get(size, 0)
    add_on_price = 0.5 * len(add_ons)
    total = base_price + add_on_price

    print("\n--- Coffee Shop Receipt ---")
    print(f"Drink: {drink_type.title()} ({size.title()}) - ${base_price}")
    if add_ons:
        print("Add-ons:", ", ".join(add_ons), f"(${add_on_price:.2f})")
    print(f"Total Price: ${total:.2f}")
    return total



calculate_order("coffee", "large", ["sugar", "cream"])