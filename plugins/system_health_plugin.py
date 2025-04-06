import psutil

def run_plugin(goal_description):
    print(f"Running plugin for goal: {goal_description}")

    # Example: Monitor CPU and memory usage
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")

        # Save the system health data to a file
        with open('system_health_log.txt', 'a') as f:
            f.write(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%\n")
        print("\nSystem health data saved to 'system_health_log.txt'")
    except Exception as e:
        print(f"Error during plugin execution: {e}")

