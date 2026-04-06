import tkinter as tk
import random


self.root = root
self.root.title("DVD Bouncing Logo")
self.width = 800
self.height = 600
self.root.geometry(f"{self.width}x{self.height}")

# Setup black background canvas
self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black', highlightthickness=0)
self.canvas.pack()

# Rectangle settings
self.rect_w, self.rect_h = 100, 60
self.x = random.randint(0, self.width - self.rect_w)
self.y = random.randint(0, self.height - self.rect_h)
self.dx, self.dy = 3, 3  # Speed/Direction

self.colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
self.current_color = random.choice(self.colors)

# Create the rectangle and text
self.rect = self.canvas.create_rectangle(
    self.x, self.y, self.x + self.rect_w, self.y + self.rect_h, 
    fill=self.current_color, outline=""
)
self.text = self.canvas.create_text(
    self.x + self.rect_w/2, self.y + self.rect_h/2, 
    text="DVD", fill="black", font=("Arial", 16, "bold")
)

self.animate()

