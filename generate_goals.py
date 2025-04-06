import json
import os

def generate_goals():
    try:
        # Ensure reflections.json exists
        if not os.path.exists('reflections.json'):
            print("❌ Error: reflections.json file not found.")
            return
        
        # Load the reflections file
        with open('reflections.json', 'r') as file:
            data = json.load(file)
        
        goals = []
        for entry in data:
            if entry['score'] <= 5:
                goal = {
                    "description": f"Improve handling of {entry['description']}",
                    "priority": entry['score'],  # Lower score = higher priority
                    "completed": False
                }
                goals.append(goal)
        
        # Sort goals by priority (lowest score = highest priority)
        goals.sort(key=lambda x: x['priority'])

        # Save the goals to goals.json
        with open('goals.json', 'w') as file:
            json.dump(goals, file, indent=4)
        
        print(f"✅ Generated {len(goals)} goals.")
    except json.JSONDecodeError:
        print("❌ Error: Could not parse reflections.json. Please check the file format.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

