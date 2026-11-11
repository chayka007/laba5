import tkinter as tk

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operation = operation_var.get()

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        else:
            result = a / b

        if result == int(result):
            result_label.config(text=f"Результат: {int(result)}")
        else:
            result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Введите корректные числа")
    except ZeroDivisionError:
        result_label.config(text="Деление на ноль")


root = tk.Tk()
root.title("Калькулятор")

entry_a = tk.Entry(root)
entry_a.pack()

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack()

entry_b = tk.Entry(root)
entry_b.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="Результат: ")
result_label.pack()

root.mainloop()