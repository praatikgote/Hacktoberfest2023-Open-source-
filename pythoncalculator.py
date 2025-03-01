import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for the display
entry = tk.Entry(window, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 20), command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 20), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 20), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI
window.mainloop()
