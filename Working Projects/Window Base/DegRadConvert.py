"""
Program Title: Degree / Radian Converter
Author: Hunter Brown
Date Created: (01/01/2024)
Last Modified: (03/27/2024)
Description: Window-Based Program used to Convert Degrees to Radians and vice versa
Usage: python DegRadConvert.py
Dependencies: Self-Contained
License: None
FIXME- DEV Notes: Pi Value is Placed Incorrectly, Pi is associated to the numerator
FIXME- ERRORS: ---
Error History Below
"""
#------------------------------------------------------------------------------


# Modules / Functions
import math
import tkinter as tk
from fractions import Fraction


def degrees_to_radians(degrees):
    try:
        radians = degrees * (math.pi / 180)
        radians_fraction = Fraction(radians / math.pi).limit_denominator()
        user_result.config(text=f' {degrees} Degrees are Equal to {radians_fraction} * π Radians ')
    except ValueError:
        user_result.config(text="Invalid Input Format")


def radians_to_degrees(radians):
    try:
        degrees = radians * (180 / math.pi)
        degrees = float(degrees)
        user_result.config(text=f' {radians} Radians are Equal to {degrees:.2f} Degrees ')
    except ValueError:
        user_result.config(text="Invalid Input Format")


# Program Window
main_window = tk.Tk()
main_window.title("")
# Instructions / Components
label_instruction = tk.Label(main_window, text="--Enter Input in Decimal Format--")
label_instruction.pack(pady=10)
# Entry Bar
user_num = tk.Entry(main_window,)
user_num.pack(padx=20, pady=10)
# Buttons
button_calculate1 = tk.Button(main_window, text=" Degree to Radian ",
                              command=lambda: degrees_to_radians(float(user_num.get())))
button_calculate1.pack(pady=10)
button_calculate2 = tk.Button(main_window, text=" Radian to Degree ",
                              command=lambda: radians_to_degrees(float(user_num.get())))
button_calculate2.pack(pady=10)
# Result
user_result = tk.Label(main_window, text="")
user_result.pack(pady=10)
main_window.mainloop()
