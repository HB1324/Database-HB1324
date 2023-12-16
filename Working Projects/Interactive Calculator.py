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

operator = input("Please select an operation: ")

if operator == ("+", "-", "*", "/"):
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

    else:
        print("Invalid Keystroke Detected... Program Terminated")
else:
    print("Invalid Keystroke Detected... Program Terminated")
