import os

def run_plugin(goal_description):
    print(f"Running plugin for: {goal_description}")
    # Custom functionality for the plugin can be added here
    with open('file_list.txt', 'w') as output_file:
        output_file.write(f"List of files for goal: {goal_description}\n")
        for root, dirs, files in os.walk("."):
            for file in files:
                output_file.write(f"{file}\n")
    print("Plugin executed successfully!")

