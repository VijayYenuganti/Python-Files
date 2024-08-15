from tkinter import *

window = Tk()
window.title("Weight Converter")

def from_kg():
    kg = float(e2_value.get())
    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274

    t1.delete("1.0", END)
    t1.insert(END, round(gram, 2))

    t2.delete("1.0", END)
    t2.insert(END, round(pound, 2))

    t3.delete("1.0", END)
    t3.insert(END, round(ounce, 2))

# Create and place widgets
e1 = Label(window, text="Enter the Weight in Kgs")
e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=1, column=2, padx=10, pady=10)

e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")

e3.grid(row=2, column=0, padx=10, pady=10)
e4.grid(row=2, column=1, padx=10, pady=10)
e5.grid(row=2, column=2, padx=10, pady=10)

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

t1.grid(row=3, column=0, padx=10, pady=10)
t2.grid(row=3, column=1, padx=10, pady=10)
t3.grid(row=3, column=2, padx=10, pady=10)

window.mainloop()
