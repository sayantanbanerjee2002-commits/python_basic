def calculate_energy_cost(appliances_usage):
    
    
    # Cost per kilowatt-hour (kWh)
    cost_per_kwh = 0.12
    
    # Dictionary to store results for each appliance
    appliance_data = {}
    
    # Variables to track totals
    total_kwh = 0
    total_cost = 0
    
    print("=" * 60)
    print("HOUSEHOLD ENERGY CONSUMPTION REPORT")
    print("=" * 60)
    print()
    
    #  Calculate consumption and cost for each appliance
    for appliance_name, usage in appliances_usage.items():
        # Extract watts and hours from the dictionary
        watts = usage["watts"]
        hours = usage["hours"]
        
        # Calculate daily kWh consumption
        kwh_per_day = (watts * hours) / 1000
        
        # Calculate daily cost
        daily_cost = kwh_per_day * cost_per_kwh
        
        # Store the results in our dictionary
        appliance_data[appliance_name] = {
            "kwh": kwh_per_day,
            "cost": daily_cost
        }
        
        # Add to totals
        total_kwh += kwh_per_day
        total_cost += daily_cost
    
    #  Calculate percentage contribution for each appliance
    print("DAILY CONSUMPTION BREAKDOWN:")
    print("-" * 60)
    
    for appliance_name, data in appliance_data.items():
        # Calculate what percentage this appliance contributes to total cost
        percentage = (data["cost"] / total_cost) * 100
        
        # Store percentage back in our data
        appliance_data[appliance_name]["percentage"] = percentage
        
        # Display the information
        print(f"{appliance_name}:")
        print(f"  Energy Used: {data['kwh']:.2f} kWh")
        print(f"  Daily Cost: ${data['cost']:.2f}")
        print(f"  Contribution: {percentage:.1f}% of total bill")
        print()
    
    # Step 3: Display total consumption and cost
    print("-" * 60)
    print(f"TOTAL DAILY CONSUMPTION: {total_kwh:.2f} kWh")
    print(f"TOTAL DAILY COST: ${total_cost:.2f}")
    print(f"MONTHLY COST (30 days): ${total_cost * 30:.2f}")
    print("=" * 60)
    print()
    
    # Suggest which appliance to optimize for 20% savings
    print("OPTIMIZATION SUGGESTION:")
    print("-" * 60)
    
    # reduction in total cost
    target_savings = total_cost * 0.20
    
    # Sort appliances by cost (highest to lowest)
    sorted_appliances = sorted(appliance_data.items(), 
                              key=lambda x: x[1]["cost"], 
                              reverse=True)
    
    print(f"To save 20% on your bill, you need to reduce costs by ${target_savings:.2f}/day")
    print()
    
    # Find which appliance(s) should be optimized
    print("RECOMMENDATION:")
    highest_cost_appliance = sorted_appliances[0][0]
    highest_cost = sorted_appliances[0][1]["cost"]
    highest_percentage = sorted_appliances[0][1]["percentage"]
    
    print(f"Focus on: {highest_cost_appliance}")
    print(f"Current cost: ${highest_cost:.2f}/day ({highest_percentage:.1f}% of bill)")
    print()
    
    # Calculate how much to reduce this appliance's usage
    reduction_needed = (target_savings / highest_cost) * 100
    
    if reduction_needed <= 100:
        print(f"Reduce {highest_cost_appliance} usage by {reduction_needed:.1f}%")
        print(f"This will save you ${target_savings:.2f}/day or ${target_savings * 30:.2f}/month")
    else:
        print(f"Reducing {highest_cost_appliance} alone won't achieve 20% savings.")
        print(f"You need to optimize multiple appliances:")
        print(f"  - Reduce {sorted_appliances[0][0]} usage")
        print(f"  - Reduce {sorted_appliances[1][0]} usage")
    
    print("=" * 60)
    
    return appliance_data, total_cost


# Sample usage with the given data
appliances_usage = {
    "AC": {"watts": 1500, "hours": 8},
    "Refrigerator": {"watts": 200, "hours": 24},
    "TV": {"watts": 150, "hours": 5}
}

# Call the function
results, total = calculate_energy_cost(appliances_usage)
