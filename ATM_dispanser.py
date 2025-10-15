def dispense_cash(amount, available_notes):
    sorted_denoms = sorted(available_notes.keys(), reverse=True)
    dispensed = {}
    remaining = amount
    
    for denom in sorted_denoms:
        
        notes_needed = remaining // denom  
        
        notes_available = available_notes[denom]
        
        notes_to_dispense = min(notes_needed, notes_available)
        
        if notes_to_dispense > 0:
            dispensed[denom] = notes_to_dispense
            remaining = remaining - notes_to_dispense * denom  
    
    
    if remaining > 0:
        return f"Error: Cannot dispense exact amount of ₹{amount}. Short by ₹{remaining}"
    
    
    for denom, count in dispensed.items():
        available_notes[denom] -= count
    
    return dispensed


print("=" * 60)
print("ATM CASH DISPENSER SIMULATION")
print("=" * 60)


atm_notes = {500: 10, 200: 20, 100: 50, 50: 30}
print("\nInitial ATM Notes Available:")
for denom, count in sorted(atm_notes.items(), reverse=True):
    print(f"  ₹{denom} notes: {count} (Total: ₹{denom * count})")

total_cash = sum(denom * count for denom, count in atm_notes.items())
print(f"\nTotal Cash in ATM: ₹{total_cash}")
#Test case :1
print("\n" + "-" * 60)
print("TEST CASE 1: Withdrawing ₹2,350")
print("-" * 60)
amount1 = 2350
result1 = dispense_cash(amount1, atm_notes)
print(f"\nWithdrawal Amount: ₹{amount1}")
print("Notes Dispensed:")
if isinstance(result1, dict):
    total_notes = 0
    for denom, count in sorted(result1.items(), reverse=True):
        print(f"  ₹{denom} × {count} = ₹{denom * count}")
        total_notes += count
    print(f"\nTotal Notes Dispensed: {total_notes}")
else:
    print(result1)

print("\nRemaining ATM Notes:")
for denom, count in sorted(atm_notes.items(), reverse=True):
    print(f"  ₹{denom} notes: {count} (Total: ₹{denom * count})")

# Test case :2
print("\n" + "-" * 60)
print("TEST CASE 2: Withdrawing ₹1,500")
print("-" * 60)
amount2 = 1500
result2 = dispense_cash(amount2, atm_notes)
print(f"\nWithdrawal Amount: ₹{amount2}")
print("Notes Dispensed:")
if isinstance(result2, dict):
    total_notes = 0
    for denom, count in sorted(result2.items(), reverse=True):
        print(f"  ₹{denom} × {count} = ₹{denom * count}")
        total_notes += count
    print(f"\nTotal Notes Dispensed: {total_notes}")
else:
    print(result2)

print("\nRemaining ATM Notes:")
for denom, count in sorted(atm_notes.items(), reverse=True):
    print(f"  ₹{denom} notes: {count} (Total: ₹{denom * count})")

