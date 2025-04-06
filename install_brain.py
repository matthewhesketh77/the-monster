import os
import shutil
import sys

def install_new_brain(filename):
    """
    Install a new brain module by copying it to the appropriate directory.
    No prompts for naming - filename passed via argument.
    """
    # Ensure the filename is passed as an argument
    if len(sys.argv) < 2:
        print("Error: No filename provided.")
        sys.exit(1)

    # Use the filename passed via command-line argument
    filename = sys.argv[1]

    # Define the destination directory (you can modify this if needed)
    destination_dir = "brains"
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copy the new brain module to the destination
    try:
        shutil.copy(filename, destination_dir)
        print(f"✅ Brain module {filename} installed successfully.")
    except Exception as e:
        print(f"❌ Error installing brain module: {str(e)}")

