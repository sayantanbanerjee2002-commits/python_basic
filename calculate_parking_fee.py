from datetime import datetime

def calculate_parking_fee(entry_time, exit_time, vehicle_type):
    
    print("\n --- Parking Fee Calculator ---")
    print(f"Entry Time: {entry_time} | Exit Time: {exit_time} | Vehicle: {vehicle_type}")

    
    rates = {"car": 3, "motorcycle": 2, "truck": 5}

    
    vehicle_type = vehicle_type.lower()
    if vehicle_type not in rates:
        print(" Invalid vehicle type.")
        return None

    fmt = "%H:%M"
    t1 = datetime.strptime(entry_time, fmt)
    t2 = datetime.strptime(exit_time, fmt)

    
    if t2 < t1:
        t2 = t2.replace(day=t2.day + 1)

    
    duration_hours = (t2 - t1).seconds / 3600
    print(f"Total Duration: {duration_hours:.2f} hours")

   
    if duration_hours <= 1:
        print(" First hour free! No charge.")
        return 0

    billable_hours = duration_hours - 1
    rate = rates[vehicle_type]
    total_fee = billable_hours * rate

   
    total_fee = round(total_fee, 2)
    print(f"Total Parking Fee: ${total_fee:.2f}")

    return total_fee



calculate_parking_fee("14:00", "18:30", "car")
calculate_parking_fee("09:15", "09:45", "motorcycle")
calculate_parking_fee("22:30", "01:00", "truck")