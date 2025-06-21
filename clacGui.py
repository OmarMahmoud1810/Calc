import customtkinter as ctk


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("green") 


app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("300x400")
app.resizable(False, False)

expression = ""

def update_expression(symbol):
    global expression
    expression += str(symbol)
    entry_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

def backspace():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

entry_var = ctk.StringVar()
entry = ctk.CTkEntry(app, textvariable=entry_var, font=("Arial", 24), width=280, justify='right')
entry.pack(pady=20)


button_frame = ctk.CTkFrame(app)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]

for row in buttons:
    row_frame = ctk.CTkFrame(button_frame)
    row_frame.pack(pady=5)
    for btn in row:
        if btn == "=":
            b = ctk.CTkButton(row_frame, text=btn, width=50, command=calculate)
        else:
            b = ctk.CTkButton(row_frame, text=btn, width=50, command=lambda x=btn: update_expression(x))
        b.pack(side="left", padx=5)


bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(pady=10)

ctk.CTkButton(bottom_frame, text="C", width=80, command=clear).pack(side="left", padx=10)
ctk.CTkButton(bottom_frame, text="⌫", width=80, command=backspace).pack(side="left", padx=10)

app.mainloop()
