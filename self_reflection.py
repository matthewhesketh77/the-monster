import json
import random

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

Q_table = {}

def initialize_q_table(goals):
    global Q_table
    for goal in goals:
        state = goal['description']
        Q_table[state] = {0: 0, 1: 0}  # Q-value for each action

def update_q_table(state, action, reward):
    old_q_value = Q_table[state][action]
    best_next_action = max(Q_table[state].values())
    new_q_value = old_q_value + alpha * (reward + gamma * best_next_action - old_q_value)
    Q_table[state][action] = new_q_value

def choose_action(state):
    if random.uniform(0, 1) < epsilon:  # Exploration
        return random.choice([0, 1])
    else:  # Exploitation
        return max(Q_table[state], key=Q_table[state].get)

def generate_new_goals(goals):
    """Generate new goals based on current reflection."""
    new_goals = []
    for goal in goals:
        if goal["completed"] and goal["priority"] < 5:
            new_goal = {
                "description": f"Improve performance on: {goal['description']}",
                "priority": goal["priority"] + 1,
                "completed": False
            }
            new_goals.append(new_goal)
    return new_goals

def self_reflection():
    try:
        with open('goals.json', 'r') as f:
            goals = json.load(f)

        if not goals:
            print("❌ No goals found.")
            return

        completed_goals = [goal for goal in goals if goal['completed']]
        uncompleted_goals = [goal for goal in goals if not goal['completed']]

        print(f"\nCompleted {len(completed_goals)} goals and {len(uncompleted_goals)} goals remain.")
        
        rewards = len(completed_goals) * 10
        penalties = len(uncompleted_goals) * -5

        print(f"Total reward points: {rewards}, Total penalty points: {penalties}")

        initialize_q_table(goals)

        for goal in goals:
            state = goal['description']
            current_priority = goal['priority']
            reward = 10 if goal['completed'] else -5
            action = choose_action(state)
            update_q_table(state, action, reward)
            goal['priority'] = action  # Assign the chosen action as the new priority

        # Generate new goals based on completed ones
        new_goals = generate_new_goals(goals)
        goals.extend(new_goals)

        # Save the updated goals back to the file after reflection
        with open('goals.json', 'w') as f:
            json.dump(goals, f, indent=4)

        print("Goals have been updated successfully!")

    except Exception as e:
        print(f"Error during reflection: {e}")

