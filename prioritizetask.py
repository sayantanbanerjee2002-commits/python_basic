def prioritize_tasks(tasks):
    
    # Step 1: Calculate priority score for each task
    for task in tasks:
        urgency = task["urgency"]
        importance = task["importance"]
        deadline = task["deadline_hours"]
        priority_score = (urgency * importance) / deadline
        
        # Add the priority score to the task dictionary
        task["priority_score"] = priority_score
    
    # Step 2: Sort tasks by priority score 
    sorted_tasks = sorted(tasks, key=lambda x: x["priority_score"], reverse=True)
    
    # Step 3: Display results with recommendations
    print("=" * 70)
    print("TASK PRIORITIZATION REPORT")
    print("=" * 70)
    print()
    
    for i, task in enumerate(sorted_tasks, 1):# sorted tasks is a list and enumerate gives both index and index,where index is start from 1 instead of o
        print(f"Rank #{i}: {task['task']}")
        print(f"  Urgency: {task['urgency']}/10")
        print(f"  Importance: {task['importance']}/10")
        print(f"  Deadline: {task['deadline_hours']} hours")
        print(f"  Priority Score: {task['priority_score']:.2f}")
        
        #  recommendations based on rank
        if i == 1:
            print(f"  ⭐ RECOMMENDATION: Do this FIRST!")
        elif i == 2:
            print(f"  📌 RECOMMENDATION: Do this next")
        else:
            print(f"  📋 RECOMMENDATION: Do this when higher priorities are done")
        
        print()
    
    
    return sorted_tasks



if __name__ == "__main__":
    # Sample task data
    tasks = [
        {"task": "Team meeting", "urgency": 8, "importance": 9, "deadline_hours": 2},
        {"task": "Email reply", "urgency": 6, "importance": 5, "deadline_hours": 24},
        {"task": "Project report", "urgency": 9, "importance": 10, "deadline_hours": 4}
    ]
    
    # function call
    prioritized = prioritize_tasks(tasks)
    
    # Show summary
    print("=" * 70)
    print("SUMMARY: Order of execution")
    print("=" * 70)
    for i, task in enumerate(prioritized, 1):
        print(f"{i}. {task['task']} (Score: {task['priority_score']:.2f})")