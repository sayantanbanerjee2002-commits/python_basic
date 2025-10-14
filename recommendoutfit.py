
def recommend_outfit(temperature, condition, occasion):
 
    
    # three dictionary to store outfit bassed on the ocassaion
    casual_outfits = {
        "hot": {
            "top": "Light cotton t-shirt or tank top",
            "bottom": "Shorts or light cotton pants",
            "footwear": "Sandals or canvas sneakers"
        },
        "warm": {
            "top": "T-shirt or casual shirt",
            "bottom": "Jeans or chinos",
            "footwear": "Sneakers or loafers"
        },
        "cool": {
            "top": "Long-sleeve shirt or light sweater",
            "bottom": "Jeans or trousers",
            "footwear": "Closed shoes or boots"
        },
        "cold": {
            "top": "Warm hoodie or jacket with inner layers",
            "bottom": "Jeans or warm pants",
            "footwear": "Boots or warm sneakers"
        }
    }
    
    formal_outfits = {
        "hot": {
            "top": "Light formal shirt (short-sleeve acceptable)",
            "bottom": "Dress pants or formal trousers",
            "footwear": "Formal leather shoes (breathable)"
        },
        "warm": {
            "top": "Formal shirt with optional blazer",
            "bottom": "Dress pants or formal trousers",
            "footwear": "Leather formal shoes"
        },
        "cool": {
            "top": "Formal shirt with blazer or suit jacket",
            "bottom": "Dress pants or formal trousers",
            "footwear": "Leather formal shoes"
        },
        "cold": {
            "top": "Formal shirt with suit and overcoat",
            "bottom": "Dress pants or formal trousers",
            "footwear": "Leather formal shoes with warm socks"
        }
    }
    
    sports_outfits = {
        "hot": {
            "top": "Moisture-wicking sleeveless jersey or light sports t-shirt",
            "bottom": "Sports shorts",
            "footwear": "Sports shoes with good ventilation"
        },
        "warm": {
            "top": "Sports t-shirt or athletic jersey",
            "bottom": "Sports shorts or track pants",
            "footwear": "Sports/running shoes"
        },
        "cool": {
            "top": "Long-sleeve sports shirt or light jacket",
            "bottom": "Track pants or sports leggings",
            "footwear": "Sports shoes with ankle support"
        },
        "cold": {
            "top": "Thermal sports wear with jacket",
            "bottom": "Thermal track pants or leggings",
            "footwear": "Insulated sports shoes"
        }
    }
    
    # Determine temperature category
    if temperature >= 28:
        temp_category = "hot"
        temp_description = "Hot"
    elif temperature >= 20:
        temp_category = "warm"
        temp_description = "Warm"
    elif temperature >= 10:
        temp_category = "cool"
        temp_description = "Cool"
    else:
        temp_category = "cold"
        temp_description = "Cold"
    
    # Select outfit based on occasion
    if occasion.lower() == "casual":
        base_outfit = casual_outfits[temp_category]
        occasion_type = "Casual"
    elif occasion.lower() == "formal":
        base_outfit = formal_outfits[temp_category]
        occasion_type = "Formal"
    elif occasion.lower() == "sports":
        base_outfit = sports_outfits[temp_category]
        occasion_type = "Sports"
    else:
        return {"error": "Invalid occasion. Choose from: casual, formal, sports"}
    
    # Start building recommendation
    recommendation = {
        "weather_info": f"{temp_description} ({temperature}°C) and {condition}",
        "occasion": occasion_type,
        "top_wear": base_outfit["top"],
        "bottom_wear": base_outfit["bottom"],
        "footwear": base_outfit["footwear"],
        "accessories": []
    }
    
    # Add weather-specific accessories and modifications
    if condition.lower() == "sunny":
        recommendation["accessories"].append("Sunglasses")
        recommendation["accessories"].append("Sunscreen")
        if temperature >= 28:
            recommendation["accessories"].append("Hat or cap for sun protection")
            recommendation["accessories"].append("Water bottle")
    
    elif condition.lower() == "rainy":
        recommendation["accessories"].append("Umbrella")
        recommendation["accessories"].append("Rain jacket or windbreaker")
        recommendation["footwear"] = "Waterproof shoes or boots"
        if occasion.lower() == "formal":
            recommendation["accessories"].append("Plastic cover for formal wear")
    
    elif condition.lower() == "cloudy":
        recommendation["accessories"].append("Light jacket")
        if temperature < 20:
            recommendation["accessories"].append("Umbrella ")
    
    elif condition.lower() == "snowy":
        recommendation["accessories"].append("Warm scarf")
        recommendation["accessories"].append("Gloves or mittens")
        recommendation["accessories"].append("Beanie or warm hat")
        recommendation["footwear"] = "Insulated waterproof boots"
        recommendation["top_wear"] = recommendation["top_wear"] + " + Heavy winter coat"
        if occasion.lower() == "sports":
            recommendation["accessories"].append("Thermal base layer recommended")
    
    else:
        recommendation["accessories"].append("Check weather updates")
    
    # Add extra layer suggestion for cold weather
    if temperature < 15 and condition.lower() != "snowy":
        recommendation["extra_tip"] = "Consider carrying an extra layer (sweater/jacket)"
    
    return recommendation


# Test the function with different scenarios
print("=" * 70)
print("WEATHER-BASED OUTFIT RECOMMENDATION SYSTEM")
print("=" * 70)

# Scenario 1: Hot sunny day, casual outing
print(" SCENARIO 1: Hot Sunny Day - Casual Outing")
print("-" * 70)
outfit1 = recommend_outfit(32, "sunny", "casual")
for key, value in outfit1.items():
    if key == "accessories":
        print(f"🎒 {key.replace('_', ' ').title()}: {', '.join(value)}")
    else:
        print(f"👉 {key.replace('_', ' ').title()}: {value}")

# Scenario 2: Cold rainy day, formal event
print("\n📍 SCENARIO 2: Cold Rainy Day - Formal Event")
print("-" * 70)
outfit2 = recommend_outfit(8, "rainy", "formal")
for key, value in outfit2.items():
    if key == "accessories":
        print(f"🎒 {key.replace('_', ' ').title()}: {', '.join(value)}")
    else:
        print(f"👉 {key.replace('_', ' ').title()}: {value}")

# Scenario 3: Cool cloudy day, sports activity
print("\n📍 SCENARIO 3: Cool Cloudy Day - Sports Activity")
print("-" * 70)
outfit3 = recommend_outfit(15, "cloudy", "sports")
for key, value in outfit3.items():
    if key == "accessories":
        print(f"🎒 {key.replace('_', ' ').title()}: {', '.join(value)}")
    else:
        print(f"👉 {key.replace('_', ' ').title()}: {value}")

# Scenario 4: Freezing snowy day, casual
print("\n📍 SCENARIO 4: Freezing Snowy Day - Casual Outing")
print("-" * 70)
outfit4 = recommend_outfit(2, "snowy", "casual")
for key, value in outfit4.items():
    if key == "accessories":
        print(f"🎒 {key.replace('_', ' ').title()}: {', '.join(value)}")
    else:
        print(f"👉 {key.replace('_', ' ').title()}: {value}")

# Scenario 5: Warm sunny day, formal meeting
print("\n📍 SCENARIO 5: Warm Sunny Day - Formal Meeting")
print("-" * 70)
outfit5 = recommend_outfit(24, "sunny", "formal")
for key, value in outfit5.items():
    if key == "accessories":
        print(f"🎒 {key.replace('_', ' ').title()}: {', '.join(value)}")
    else:
        print(f"👉 {key.replace('_', ' ').title()}: {value}")

print("\n" + "=" * 70)
print("💡 TIP: You can test with your own values!")
print("Example: recommend_outfit(25, 'rainy', 'sports')")
print("=" * 70)