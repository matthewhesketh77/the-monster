import pandas as pd

def run_plugin(goal_description):
    print(f"Running plugin for goal: {goal_description}")

    # Example: Load a CSV file and analyze its content
    try:
        df = pd.read_csv('data.csv')  # Assuming there's a CSV file in the same directory
        print(f"Analyzing data from: data.csv")

        # Get basic statistics about the data
        summary = df.describe()  # Summary statistics
        print("\nData Summary:")
        print(summary)

        # Save the summary to a file
        with open('data_analysis_summary.txt', 'w') as f:
            f.write(str(summary))
        print("\nSummary saved to 'data_analysis_summary.txt'")
    except Exception as e:
        print(f"Error during plugin execution: {e}")

