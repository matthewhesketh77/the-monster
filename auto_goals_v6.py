import json
with open('reflections.json', 'r') as file:
    data = json.load(file)
goals = []
for entry in data:
    if entry['score'] <= 5:
        goals.append("Improve handling of " + entry['description'])
print(goals)
