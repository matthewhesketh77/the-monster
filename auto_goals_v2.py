```python
import json
def generate_goals():
    with open('reflections.json', 'r') as file:
        data = json.load(file)
    goals = []
    for entry in data:
        if entry['score'] <= 5:
            goal = "Improve handling of " + entry['description']
            goals.append(goal)
    return goals
```