import os
import random
import time
import tkinter as tk
import threading

# --- EDIT THESE VALUES ---
MAX_FILES = 500        # Total number of files/popups
SPEED = 0.01           # How fast they spawn (seconds)
# -------------------------

def create_popup(file_num, file_name):
    """Creates a standalone popup at a random screen location."""
    root = tk.Tk()
    root.title(f"Popup {file_num}")
    
    # Get screen width and height to pick a random spot
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Random window position (x, y)
    width, height = 200, 100
    x = random.randint(0, screen_width - width)
    y = random.randint(0, screen_height - height)
    
    # Set size and position: "widthxheight+x+y"
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.attributes('-topmost', True) # Keep on top

    tk.Label(root, text=f"File: {file_name}\nClick to close").pack(pady=10)
    tk.Button(root, text="Click", command=root.destroy).pack()

    root.mainloop()

def create_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"Starting... spawning {MAX_FILES} popups all over the screen.")

    for i in range(1, MAX_FILES + 1):
        # 1. Create the file
        name = "".join([str(random.randint(0, 9)) for _ in range(5)])
        file_path = os.path.join(desktop_path, f"{name}.txt")
        with open(file_path, "w") as f:
            f.write(f"File {i} of {MAX_FILES}")

        # 2. Launch popup in a separate thread so the script doesn't wait
        popup_thread = threading.Thread(target=create_popup, args=(i, name))
        popup_thread.daemon = True # Closes popups if you stop the main script
        popup_thread.start()

        print(f"[{i}/{MAX_FILES}] Created: {name}.txt")
        
        time.sleep(SPEED)

    print("\nLimit reached. Popups will stay until clicked.")
    
    # Keep the main script alive so threads don't die instantly
    while True:
        time.sleep(1)

if __name__ == "__main__":
    create_files()
