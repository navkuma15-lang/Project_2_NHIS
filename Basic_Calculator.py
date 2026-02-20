import tkinter as tk
from tkinter import messagebox

class PythonCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("360x220")
        
        # Display storage
        self.expression = ""
        self.display_text = tk.StringVar()

        # --- Entry Field (The white box at the top) ---
        self.display = tk.Entry(
            root, textvariable=self.display_text, 
            font=("Arial", 14), bd=7, relief="sunken", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=12, sticky="nsew")

        # --- Button Configuration ---
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('c', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Configure weights so buttons expand evenly
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
 
    def create_button(self, text, row, col):
        button = tk.Button(
            self.root, text=text, font=("Arial", 12),
            command=lambda: self.on_click(text),
            relief="raised", borderwidth=1
        )
        button.grid(row=row, column=col, sticky="nsew")

    def on_click(self, char):
        if char == '=':
            try:
                # Solve the math expression
                result = str(eval(self.expression))
                self.display_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.clear()
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear()
        elif char == 'c':
            self.clear()
        else:
            self.expression += str(char)
            self.display_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonCalculator(root)
    root.mainloop()