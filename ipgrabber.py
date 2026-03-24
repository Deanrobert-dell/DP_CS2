import os
import random
import time

# --- EDIT THESE VALUES ---
MAX_FILES = 1000      # Total number of files to create
SPEED = 0         # Seconds to wait between each file
# -------------------------

def create_files():
    # Path to the Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    print(f"Starting... creating {MAX_FILES} files at {SPEED}s intervals.")

    for i in range(1, MAX_FILES + 1):
        # Generate random 5-digit number
        name = "".join([str(random.randint(0, 9)) for _ in range(5)])
        file_path = os.path.join(desktop_path, f"{name}.txt")

        # Create the file
        with open(file_path, "w") as f:
            f.write(f"File {i} of {MAX_FILES}")

        print(f"[{i}/{MAX_FILES}] Created: {name}.txt")
        
        # Wait before the next one
        time.sleep(SPEED)

    print("\nDone! Limit reached.")

if __name__ == "__main__":
    create_files()

