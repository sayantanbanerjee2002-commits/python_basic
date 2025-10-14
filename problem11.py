
def apply_discounts(cart_items, coupon_code):
    original_price = 0 #calculate original price
    for item in cart_items:
        item_total = item["price"] * item["quantity"]
        original_price += item_total
    
    
    total_discount = 0 #intialize the total discount
    
    # Check if SAVE20 coupon is used (it cannot combine with other discounts)
    if coupon_code == "SAVE20":
        total_discount = original_price * 0.20  
    else:
        #  Apply cart total discount 
        if original_price > 3000:
            total_discount += original_price * 0.10
        
        # Apply clothing category discount
        for item in cart_items:
            if item["category"] == "clothing" and item["quantity"] >= 2:
                clothing_total = item["price"] * item["quantity"]
                total_discount += clothing_total * 0.15
        
        # Step 6: Apply FIRST50 coupon 
        if coupon_code == "FIRST50" and original_price >= 500:
            total_discount += 50
    
    # Step 7: Calculate final price
    final_price = original_price - total_discount
    
    
    return {
        "original_price": original_price,
        "total_discount": total_discount,
        "final_price": final_price
    }
cart_items = [
    {"name": "Shirt", "price": 500, "category": "clothing", "quantity": 2},
    {"name": "Shoes", "price": 2000, "category": "footwear", "quantity": 1}
]

print("=" * 60)
print("SHOPPING CART DISCOUNT CALCULATOR")
print("=" * 60)

# Display cart items
print("\nYour Cart:")
for item in cart_items:
    print(f"  - {item['name']}: ${item['price']} x {item['quantity']} = ${item['price'] * item['quantity']}")

print("\n" + "=" * 60)
print("\nScenario 1: No Coupon")
result1 = apply_discounts(cart_items, None)
print(f"Original Price: ${result1['original_price']}")
print(f"Total Discount: ${result1['total_discount']}")
print(f"Final Price: ${result1['final_price']}")

print("\n" + "-" * 60)    
print("\nScenario 2: Using 'FIRST50' Coupon")
result2 = apply_discounts(cart_items, "FIRST50")
print(f"Original Price: ${result2['original_price']}")
print(f"Total Discount: ${result2['total_discount']}")
print(f"Final Price: ${result2['final_price']}")

print("\n" + "-" * 60)
