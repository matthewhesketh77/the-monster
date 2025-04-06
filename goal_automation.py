import json

def process_goals():
    try:
        # Load goals from goals.json
        with open('goals.json', 'r') as file:
            goals = json.load(file)
        
        if not goals:
            print("❌ No goals to process.")
            return
        
        # Process the goals in priority order (highest priority first)
        for goal in goals:
            if not goal['completed']:
                print(f"🔧 Working on goal: {goal['description']}")
                # Simulate goal completion
                goal['completed'] = True
                print(f"✅ Goal completed: {goal['description']}")
        
        # Save updated goals back to goals.json
        with open('goals.json', 'w') as file:
            json.dump(goals, file, indent=4)
        
        print("✅ All goals processed.")
    except json.JSONDecodeError:
        print("❌ Error: Could not parse goals.json. Please check the file format.")
    except FileNotFoundError:
        print("❌ Error: goals.json file not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

process_goals()

