import tkinter as tk
import random


def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    panel.config(bg=random.choice(colors))


root = tk.Tk()
root.title("Цветная панель")

panel = tk.Frame(root, width=300, height=200, bg="white")
panel.pack(padx=10, pady=10)

tk.Button(root, text="Сменить цвет", command=change_color).pack(pady=5)

root.mainloop()