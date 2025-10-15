def calculate_calories(activity, duration_minutes, weight_kg):
   

    print("\n --- Fitness Tracker ---")
    print(f"Activity: {activity.title()} | Duration: {duration_minutes} min | Weight: {weight_kg} kg")

    
    activity_rates = {
        "running": 0.15,
        "cycling": 0.12,
        "swimming": 0.14,
        "walking": 0.07,
        "yoga": 0.05
    }

   
    activity = activity.lower()
    if activity not in activity_rates:
        print(" Invalid activity type.")
        return None

    
    rate = activity_rates[activity]
    calories_burned = rate * weight_kg * duration_minutes

    
    print(f"Total Calories Burned: {calories_burned:.2f} kcal")

    
    goal = 500
    if calories_burned >= goal:
        print(" Congratulations! You've met your daily goal of 500 calories!")
    else:
        
        remaining = goal - calories_burned
        extra_minutes = remaining / (rate * weight_kg)
        print(f"⚡ You need {extra_minutes:.1f} more minutes of {activity} to reach 500 kcal.")

    return calories_burned


calculate_calories("Running", 40, 70)
calculate_calories("Cycling", 30, 60)
calculate_calories("Yoga", 60, 65)