import json

def generate_goals():
    with open('reflections.json', 'r') as file:
        data = json.load(file)

    goals = []
    for entry in data:
        score = entry.get('score', 10)
        description = entry.get('description', 'an unknown task')
        if score <= 5:
            goal = f"Improve handling of {description}"
            goals.append(goal)

    return goals

if __name__ == "__main__":
    new_goals = generate_goals()
    print("Generated Goals:")
    for goal in new_goals:
        print("-", goal)

