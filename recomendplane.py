def recommend_plan(usage_hours, content_type, num_devices):
    
    
    # Define all available plans with their features and prices
    plans = {
        'Basic': {
            'hours': 10,
            'devices': 1,
            'quality': 'SD',
            'price': 5
        },
        'Standard': {
            'hours': 50,
            'devices': 2,
            'quality': 'HD',
            'price': 12
        },
        'Premium': {
            'hours': float('inf'),  # Unlimited hours
            'devices': 4,
            'quality': '4K',
            'price': 20
        }
    }
    
    # Overage charge per hour
    OVERAGE_RATE = 0.50
    
    # Quality hierarchy (higher quality includes lower qualities)
    quality_levels = {'SD': 1, 'HD': 2, '4K': 3}
    
    print(f"\n{'='*60}")
    print(f"USER REQUIREMENTS:")
    print(f"{'='*60}")
    print(f"🕐 Usage Hours: {usage_hours} hours/month")
    print(f"📺 Content Quality: {content_type}")
    print(f"📱 Number of Devices: {num_devices}")
    print(f"{'='*60}\n")
    
    # Store suitable plans with their costs
    suitable_plans = []
    
    # Check each plan
    for plan_name, features in plans.items():
        print(f"\n--- Analyzing {plan_name} Plan ---")
        print(f"Base Price: ${features['price']}")
        print(f"Includes: {features['hours']} hours, {features['devices']} device(s), {features['quality']} quality")
        
        # Check if plan meets device requirement
        if num_devices > features['devices']:
            print(f"❌ Not enough devices ({features['devices']} < {num_devices})")
            continue
        
        # Check if plan meets quality requirement
        if quality_levels[features['quality']] < quality_levels[content_type]:
            print(f"❌ Quality too low ({features['quality']} < {content_type})")
            continue
        
        # Calculate total cost including overage
        base_cost = features['price']
        overage_hours = 0
        overage_cost = 0
        
        # Calculate overage if hours exceed plan limit
        if usage_hours > features['hours']:
            overage_hours = usage_hours - features['hours']
            overage_cost = overage_hours * OVERAGE_RATE
        
        total_cost = base_cost + overage_cost
        
        print(f"✅ Plan meets requirements!")
        if overage_hours > 0:
            print(f"⚠️  Overage: {overage_hours} hours × ${OVERAGE_RATE}/hour = ${overage_cost:.2f}")
        print(f"💵 Total Cost: ${total_cost:.2f}")
        
        # Store this plan as a suitable option
        suitable_plans.append({
            'name': plan_name,
            'total_cost': total_cost,
            'base_cost': base_cost,
            'overage_hours': overage_hours,
            'overage_cost': overage_cost
        })
    
    # Find the best (cheapest) plan
    if not suitable_plans:
        print("\n❌ No suitable plan found for your requirements!")
        return None
    
    # Sort plans by total cost and get the cheapest
    best_plan = min(suitable_plans, key=lambda x: x['total_cost'])
    
    # Display recommendation
    print(f"\n{'='*60}")
    print(f"🎉 RECOMMENDATION:")
    print(f"{'='*60}")
    print(f"Best Plan: {best_plan['name']}")
    print(f"Base Price: ${best_plan['base_cost']}")
    
    if best_plan['overage_hours'] > 0:
        print(f"Overage Fee: ${best_plan['overage_cost']:.2f} ({best_plan['overage_hours']} extra hours)")
    
    print(f"Total Monthly Cost: ${best_plan['total_cost']:.2f}")
    print(f"{'='*60}\n")
    
    # Show comparison if multiple plans are suitable
    if len(suitable_plans) > 1:
        print("Other suitable options:")
        for plan in suitable_plans:
            if plan['name'] != best_plan['name']:
                print(f"  • {plan['name']}: ${plan['total_cost']:.2f}")
    
    return best_plan
# test cases :
print("\n" + "🔷"*30)
print("TEST CASE 1: Light User")
print("🔷"*30)
recommend_plan(8, 'SD', 1)

print("\n" + "🔷"*30)
print("TEST CASE 2: Moderate User with Overage")
print("🔷"*30)
recommend_plan(25, 'HD', 2)

print("\n" + "🔷"*30)
print("TEST CASE 3: Heavy User")
print("🔷"*30)
recommend_plan(80, '4K', 3)

print("\n" + "🔷"*30)
print("TEST CASE 4: Basic Plan with Heavy Overage")
print("🔷"*30)
recommend_plan(40, 'SD', 1)
