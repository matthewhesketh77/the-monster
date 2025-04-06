import json
import time
import random

# Function to check if all goals are completed
def check_all_goals_completed():
    try:
        with open("goals.json", "r") as f:
            goals = json.load(f)
        completed_goals = [goal for goal in goals if goal.get("completed", False)]
        completion_rate = len(completed_goals) / len(goals) if len(goals) > 0 else 0
        print(f"Completed goals: {len(completed_goals)} / Total goals: {len(goals)}")
        return completion_rate == 1
    except Exception as e:
        print(f"Error checking goals: {e}")
        return False

# Function to process goals and mark them as completed
def process_goal(goal):
    try:
        print(f"Processing goal: {goal['description']}")
        # Add your goal processing logic here
        goal["completed"] = True  # Mark the goal as completed
        print(f"Goal completed: {goal['description']}")
        
        # Save the updated goal list back to the file
        with open("goals.json", "r") as f:
            goals = json.load(f)
        
        # Update the goal list
        for i, g in enumerate(goals):
            if g["description"] == goal["description"]:
                goals[i] = goal
        
        with open("goals.json", "w") as f:
            json.dump(goals, f, indent=4)
        print(f"Updated goal: {goal['description']}")
    except Exception as e:
        print(f"Error processing goal: {e}")

# Function to load and run the plugins
def load_and_run_plugins():
    try:
        with open("goals.json", "r") as f:
            goals = json.load(f)
        
        # Iterate over each goal and run the associated plugin
        for goal in goals:
            if not goal["completed"]:
                print(f"Running plugin for goal: {goal['description']}")
                process_goal(goal)  # Process the goal to mark it as completed
        
    except Exception as e:
        print(f"Error loading and running plugins: {e}")

# Main loop function to control the Monster's cycle
def main_loop():
    cycle_count = 0

    while True:  # Run the loop indefinitely
        cycle_count += 1
        print(f"--- MONSTER LOOP CYCLE {cycle_count} ---")
        
        # Step 1: Evolving new module
        print("[1] EVOLVING NEW MODULE...")
        time.sleep(0.1)  # Simulate evolving module
        print("New brain output written to brain_output.txt")

        # Step 2: Generate new goals from reflections
        print("[3] GENERATING GOALS FROM REFLECTIONS...")
        time.sleep(1)  # Simulate goal generation

        # Step 3: Processing high-priority goals
        print("[4] PROCESSING HIGH-PRIORITY GOALS...")
        load_and_run_plugins()  # Call function to process goals
        print("All high-priority goals processed.")

        # Step 4: Self-reflection and adaptive learning
        print("[5] SELF-REFLECTION AND ADAPTIVE LEARNING...")
        time.sleep(1)  # Simulate self-reflection

        # Log the current cycle to the log file
        cycle_data = {
            "cycle_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "goals_completed": check_all_goals_completed()
        }

        try:
            with open("log.json", "r") as f:
                logs = json.load(f)
        except:
            logs = []

        logs.append(cycle_data)

        with open("log.json", "w") as f:
            json.dump(logs, f, indent=4)

        print(f"[{cycle_count}] Cycle {cycle_count} logged.")

# Start the main loop
if __name__ == "__main__":
    main_loop()

