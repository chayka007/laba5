import tkinter as tk


def on_exit():
    root.destroy()


root = tk.Tk()
root.title("Окно с меню")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

tk.Label(root, text="Выберите File -> Exit, чтобы закрыть окно").pack(padx=20, pady=20)

root.mainloop()