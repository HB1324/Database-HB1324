"""
Program Title: Age Calculator
Author: Hunter Brown
Date Created: (01/01/2024)
Last Modified: (03/27/2024)
Description: Window-Based Program Used to calculate user age
Usage: python AgeCalc02.py
Dependencies: Self-Contained
License: None
FIXME- DEV Notes: ---
FIXME- ERRORS: ---
Error History Below
"""
#------------------------------------------------------------------------------
import tkinter as tk
from datetime import datetime


def calculate_age():
    birth_date = entry_birth_date.get()

    try:
        birth_date = datetime.strptime(birth_date, '%m-%d-%Y')
        current_date = datetime.now()
        age = current_date.year - birth_date.year - (
                    (current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        label_result.config(text=f"Your age is: {age} years")
    except ValueError:
        label_result.config(text="Invalid date format. Please use YYYY-MM-DD.")


# Create the main window
window = tk.Tk()
window.title("Age Calculator")

# Create and place widgets
label_instruction = tk.Label(window, text="Enter your birthdate (MM-DD-YYYY):")
label_instruction.pack(pady=10)

entry_birth_date = tk.Entry(window)
entry_birth_date.pack(pady=10)

button_calculate = tk.Button(window, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=10)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
