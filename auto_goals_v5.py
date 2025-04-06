import json

def generate_goals():
    with open('reflections.json', 'r') as file:
        data = json.load(file)
    
    goals = []
    for entry in data:
        if entry['score'] <= 5:
            description = entry['description']
            goal_string = f"Improve handling of {description}"
            goals.append(goal_string)
    
    return goals
