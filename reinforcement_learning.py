import random
import json

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Initialize Q-table (for now, this will be a simple dictionary)
Q_table = {}

# Initialize actions and states (goals and priority levels)
def initialize_q_table(goals):
    global Q_table
    for goal in goals:
        # State: goal description
        state = goal['description']
        # Action: change priority (0 = low, 1 = high)
        Q_table[state] = {0: 0, 1: 0}  # Q-value for each action (low or high priority)

def update_q_table(state, action, reward):
    old_q_value = Q_table[state][action]
    best_next_action = max(Q_table[state].values())
    new_q_value = old_q_value + alpha * (reward + gamma * best_next_action - old_q_value)
    Q_table[state][action] = new_q_value

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        # Exploration: choose a random action
        return random.choice([0, 1])
    else:
        # Exploitation: choose the best action (highest Q-value)
        return max(Q_table[state], key=Q_table[state].get)

def self_reflection_with_qlearning():
    try:
        with open('goals.json', 'r') as f:
            goals = json.load(f)

        if not goals:
            print("❌ No goals found.")
            return

        # Initialize Q-table with goals
        initialize_q_table(goals)

        for goal in goals:
            state = goal['description']
            current_priority = goal['priority']
            reward = 10 if goal['completed'] else -5

            # Choose action based on current state
            action = choose_action(state)
            print(f"Goal: {goal['description']} | Action: {action} | Reward: {reward}")

            # Update Q-table with new action
            update_q_table(state, action, reward)

            # Adjust goal priority based on learned action
            goal['priority'] = action

        # Save the updated goals back to goals.json
        with open('goals.json', 'w') as f:
            json.dump(goals, f, indent=4)

    except Exception as e:
        print(f"❌ Error during reinforcement learning: {str(e)}")

