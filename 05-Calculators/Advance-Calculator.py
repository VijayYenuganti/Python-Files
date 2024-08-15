# Advance Calculator

from tkinter import *

root = Tk()
root.title("Adv. Calculator")
root.geometry("570x740+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""


def show(value):
    global equation
    equation += str(value)
    label.config(text=equation)


def clear():
    global equation
    equation = ""
    label.config(text="0")


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label.config(text=result)


# Label to display the input and result, aligned to the right
label = Label(root, text="0", font=("Arial", 24), bg="#fff", fg="#000", width=40, height=3, anchor='e')
label.grid(row=0, column=0, columnspan=4, padx=4, pady=8)

# Button layout using grid
buttons = [
    ('AC', 1, 0, 'clear', "#FF5733"), ('/', 1, 1, '/', "#A9A9A9"), ('%', 1, 2, '%', "#A9A9A9"), ('*', 1, 3, '*', "#A9A9A9"),
    ('7', 2, 0, '7', "#FFF"), ('8', 2, 1, '8', "#FFF"), ('9', 2, 2, '9', "#FFF"), ('-', 2, 3, '-', "#A9A9A9"),
    ('4', 3, 0, '4', "#FFF"), ('5', 3, 1, '5', "#FFF"), ('6', 3, 2, '6', "#FFF"), ('+', 3, 3, '+', "#A9A9A9"),
    ('1', 4, 0, '1', "#FFF"), ('2', 4, 1, '2', "#FFF"), ('3', 4, 2, '3', "#FFF"), ('=', 4, 3, 'calculate', "#A9A9A9", 2),
    ('0', 5, 0, '0', "#FFF", 2), ('.', 5, 2, '.', "#FFF"),
]

for (text, row, col, cmd, color, *span) in buttons:
    colspan = span[0] if span else 1
    button = Button(root, text=text, width=5, height=2, font=("Poppins", 20, "bold"), bd=1, fg="#000", bg=color,
                    command=(lambda cmd=cmd: clear() if cmd == 'clear' else calculate() if cmd == 'calculate' else show(cmd)))
    button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Configure grid to be responsive
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    if i < 4:
        root.grid_columnconfigure(i, weight=1)

root.mainloop()
