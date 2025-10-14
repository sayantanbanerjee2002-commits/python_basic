def assign_table(party_size, available_tables):
    
    print("\n --- Restaurant Table Assignment ---")
    print(f"Party size: {party_size}")
    print(f"Available tables: {available_tables}")
    suitable_tables = {t: cap for t, cap in available_tables.items() if cap >= party_size}
    if not suitable_tables:
        print("No suitable table available. Please wait.")
        return "Please wait"
    assigned_table = min(suitable_tables, key=lambda t: suitable_tables[t])
    
    print(f" Assigned Table Number: {assigned_table} (Capacity: {available_tables[assigned_table]})")
    return assigned_table


available_tables = {1: 2, 2: 4, 3: 4, 4: 6, 5: 8}

assign_table(6, available_tables)
assign_table(5, available_tables)
assign_table(9, available_tables)