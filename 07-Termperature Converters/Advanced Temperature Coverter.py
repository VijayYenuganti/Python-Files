from tkinter import *

# Initialize the main window
root = Tk()
root.title("Adv. Temperature Converter")
root.geometry("500x300+100+200")
root.resizable(False, False)
root.configure(bg="#F5F5F5")

# Variable for storing the selected radio button value
radio = IntVar()

# Function to perform the temperature conversion based on the selected option
def convert_temperature():
    temp = float(e2_value.get())
    result = ""
    
    if radio.get() == 1:
        result = f"{temp}°C = {round((temp * 9/5) + 32, 2)}°F"
    elif radio.get() == 2:
        result = f"{temp}°F = {round((temp - 32) * 5/9, 2)}°C"
    
    label_result.config(text=result)

# Function to update label based on the selected radio button
def selection():
    label_result.config(text="")

# Create and place widgets
label = Label(root, text="Enter the Temperature", font=("Arial", 16), bg="#F5F5F5")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value, font=("Arial", 14))
e2.grid(row=1, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Center the conversion button
Button_convert = Button(root, text="Convert", font=("Arial", 14), command=convert_temperature)
Button_convert.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Radiobuttons for selecting conversion type
R1 = Radiobutton(root, text="Celsius to Fahrenheit", variable=radio, value=1, font=("Arial", 12), bg="#F5F5F5", command=selection)
R2 = Radiobutton(root, text="Fahrenheit to Celsius", variable=radio, value=2, font=("Arial", 12), bg="#F5F5F5", command=selection)

R1.grid(row=2, column=0, padx=10, pady=10, sticky="w")
R2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Result label
label_result = Label(root, text="", font=("Arial", 14), bg="#F5F5F5")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Adjust column weights for centering
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
