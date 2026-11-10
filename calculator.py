import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#1e1e24")
        self.root.resizable(False, False)

        self.display_var = tk.StringVar(value="")
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(
            self.root, 
            textvariable=self.display_var, 
            font=("Segoe UI", 24), 
            bg="#222222", 
            fg="#ffffff", 
            bd=0, 
            justify="right",
            insertbackground="white"
        )
        display.pack(fill="both", ipadx=8, ipady=20, padx=20, pady=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1e1e24")
        button_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        for i in range(4):
            button_frame.columnconfigure(i, weight=1, minsize=60)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1, minsize=60)

        buttons = [
            ('C', 0, 0, '#f1a33c', 'black'), ('/', 0, 1, '#f1a33c', 'black'), 
            ('*', 0, 2, '#f1a33c', 'black'), ('DEL', 0, 3, '#f1a33c', 'black'),
            ('7', 1, 0, '#333333', 'white'), ('8', 1, 1, '#333333', 'white'), 
            ('9', 1, 2, '#333333', 'white'), ('-', 1, 3, '#f1a33c', 'black'),
            ('4', 2, 0, '#333333', 'white'), ('5', 2, 1, '#333333', 'white'), 
            ('6', 2, 2, '#333333', 'white'), ('+', 2, 3, '#f1a33c', 'black'),
            ('1', 3, 0, '#333333', 'white'), ('2', 3, 1, '#333333', 'white'), 
            ('3', 3, 2, '#333333', 'white'), ('=', 3, 3, '#2ec4b6', 'white'),
            ('0', 4, 0, '#333333', 'white'), ('.', 4, 2, '#333333', 'white')
        ]

        for text, row, col, bg, fg in buttons:
            action = lambda x=text: self.on_button_click(x)
            colspan = 2 if text == '0' else 1
            rowspan = 2 if text == '=' else 1

            btn = tk.Button(
                button_frame, text=text, font=("Segoe UI", 16),
                bg=bg, fg=fg, activebackground="#444444", activeforeground="white",
                bd=0, relief="flat", command=action
            )
            btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        current_text = self.display_var.get()

        if current_text == "Error":
            current_text = ""

        if char == 'C':
            self.display_var.set("")
        elif char == 'DEL':
            self.display_var.set(current_text[:-1])
        elif char == '=':
            try:
                if current_text.strip():
                    # Safely evaluate calculations without built-in context risk
                    result = eval(current_text, {"__builtins__": None}, {})
                    self.display_var.set(str(result))
            except Exception:
                self.display_var.set("Error")
        else:
            self.display_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
