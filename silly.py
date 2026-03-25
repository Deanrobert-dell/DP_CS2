import tkinter as tk
import random

def create_popup():
    # Create the popup window
    root = tk.Tk()
    root.title("System Error")
    
    # Randomize position so they fill the screen
    width, height = 300, 150
    x = random.randint(0, root.winfo_screenwidth() - width)
    y = random.randint(0, root.winfo_screenheight() - height)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Add a message
    label = tk.Label(root, text="A critical error occurred.\nPlease do not close this window.", padx=20, pady=20)
    label.pack()

    # The magic part: when they try to close it, spawn 5 more
    def on_closing():
        root.destroy()  # Close the current one
        for _ in range(5):
            create_popup()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

# Start the first popup
if __name__ == "__main__":
    create_popup()