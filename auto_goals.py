import json

def generate_goals():
    with open('reflections.json', 'r') as file:
        data = json.load(file)
    
    goals = []
    for task in data:
        score = task.get('score', 10)  # Default to 10 if missing
        if score <= 5:
            desc = task.get('description', 'an unknown task')
            goal = f"Improve handling of {desc.split(':')[0].strip()}."
            goals.append(goal)
    
    return goals

if __name__ == "__main__":
    new_goals = generate_goals()
    print("Generated Goals:")
    for goal in new_goals:
        print("-", goal)

