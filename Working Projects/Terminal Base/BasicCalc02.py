"""
Program Title: Basic Calculator (v0.2)
Author: Hunter Brown
Date Created: 01/2024
Last Modified: 03/27/2024
Description: Terminal-Based program for mathematical operations (+ - * /)
Usage: python BasicCalc02.py
Dependencies: Self-Contained
License: None
FIXME- DEV Notes: ---
FIXME- ERRORS: ---
Error History Below
"""
#--------------------------------------------------------------------------

def calcadd(user_num1, user_num2):
    answer = user_num1 + user_num2
    return answer

def calcsub(user_num1, user_num2):
    sub = user_num1 - user_num2
    return sub

def calcmult(user_num1, user_num2):
    mult = user_num1 * user_num2
    return mult

def calcdiv(user_num1, user_num2):
    div = user_num1 / user_num2
    return div

print("Welcome to HB's interactive calculator!")
print("* Using this format -> (+ - * /) *\n")

operator = input("Please select an operation (+ - * /): ")

if operator not in ['+', '-', '*', '/']:
    print("Invalid operator entered. Program terminated.")
else:
    user_num1st = int(input("Enter 1st Number: "))
    user_num2nd = int(input("Enter 2nd Number: "))

    if operator == "+":
        output = calcadd(user_num1st, user_num2nd)
        print("Answer: ", output)

    elif operator == "-":
        output = calcsub(user_num1st, user_num2nd)
        print("Answer: ", output)

    elif operator == "*":
        output = calcmult(user_num1st, user_num2nd)
        print("Answer: ", output)

    elif operator == "/":
        output = calcdiv(user_num1st, user_num2nd)
        print("Answer: ", output)


#------------------------------------------------------------------------------
"""
---Error History---

Incident 01
Program: BasicCalc02.py
Date:(03/27/2024)
Type: Processing / Format
Initial Error:If/Else statements were improperly formed causing program to
produce Invalid Error Handler
Solution: Removed 1st unit to confirm operation value



"""