def book_tickets(age, day, time, num_tickets):
    
    if age < 12:
        base_price = 8      
    elif age <= 64:
        base_price = 12     
    else:
        base_price = 9      

    
    if day.lower() in ["saturday", "sunday"]:
        base_price += 3
    hour = int(time.split(":")[0])
    if hour < 17:
        base_price -= 2
    total = base_price * num_tickets

    if num_tickets >= 5:
        total *= 0.9  # 10% discount

    
    print("\n --- Movie Ticket Summary ---")
    print(f"Age: {age} | Day: {day} | Time: {time}")
    print(f"Tickets: {num_tickets}")
    print(f"Base Price per Ticket: ${base_price}")
    print(f"Total Cost: ${total:.2f}")

    return total