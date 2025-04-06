import json
from plugin_loader import run_plugin

# === Load plugin index ===
with open("plugin_index.json", "r") as f:
    plugin_index = json.load(f)

# === Load plugin memory ===
try:
    with open("plugin_memory.json", "r") as f:
        plugin_memory = json.load(f)
except:
    plugin_memory = {}

# === Load tasks ===
with open("tasks.json", "r") as f:
    tasks = json.load(f)

if not tasks:
    print("No tasks found.")
    exit()

task = tasks[0]
description = task.get("description", "").lower()
args = task.get("args", {})

# === Match description to best plugin ===
matched_plugin = None
best_score = -1

for plugin, desc in plugin_index.items():
    if any(word in description for word in desc.lower().split()):
        # Check average performance score
        memory = plugin_memory.get(plugin, {"uses": 0, "total_score": 0})
        avg_score = memory["total_score"] / memory["uses"] if memory["uses"] > 0 else 1
        if avg_score > best_score:
            best_score = avg_score
            matched_plugin = plugin

if not matched_plugin:
    print("No matching plugin found.")
    exit()

# === Run the plugin ===
result = run_plugin(matched_plugin, **args)

# === Ask for rating ===
print(f"\nResult:\n{result}")
score = input(f"\nRate the usefulness of plugin '{matched_plugin}' from 1–10: ")

try:
    score = int(score)
    assert 1 <= score <= 10
except:
    print("Invalid score. Defaulting to 5.")
    score = 5

# === Save updated plugin memory ===
memory = plugin_memory.get(matched_plugin, {"uses": 0, "total_score": 0})
memory["uses"] += 1
memory["total_score"] += score
plugin_memory[matched_plugin] = memory

with open("plugin_memory.json", "w") as f:
    json.dump(plugin_memory, f, indent=2)

# === Log to reflections ===
reflection_entry = {
    "description": description,
    "plugin_used": matched_plugin,
    "args": args,
    "result": result,
    "score": score
}

try:
    with open("reflections.json", "r") as f:
        reflections = json.load(f)
except:
    reflections = []

reflections.append(reflection_entry)

with open("reflections.json", "w") as f:
    json.dump(reflections, f, indent=2)

print("\nReflection saved.")

