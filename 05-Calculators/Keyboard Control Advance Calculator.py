import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 16, "bold")


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        # Configuring grid weights to ensure buttons expand
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
            if i < 4:
                self.buttons_frame.columnconfigure(i, weight=1)

        self.create_buttons()

        # Bind keys
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.clear())
        for key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/'):
            self.window.bind(key, self.add_to_expression)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR,
                               padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, event):
        self.current_expression += str(event.char)
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == "C":
                button = tk.Button(self.buttons_frame, text=button, font=LARGE_FONT_STYLE, borderwidth=0,
                                   command=self.clear)
            elif button == "=":
                button = tk.Button(self.buttons_frame, text=button, font=LARGE_FONT_STYLE, borderwidth=0,
                                   command=self.evaluate)
            else:
                button = tk.Button(self.buttons_frame, text=button, font=LARGE_FONT_STYLE, borderwidth=0,
                                   command=lambda x=button: self.add_to_expression(tk.Event(char=x)))

            button.grid(row=row, column=col, sticky=tk.NSEW)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def clear(self, event=None):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.total_label.config(text=self.total_expression)

    def evaluate(self, event=None):
        self.total_expression = self.current_expression
        try:
            self.current_expression = str(eval(self.current_expression))
        except Exception as e:
            self.current_expression = "Error"
        self.update_label()
        self.total_label.config(text=self.total_expression)
        self.current_expression = ""

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
