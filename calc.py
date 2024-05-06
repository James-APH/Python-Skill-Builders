# Author: James Huston
# Email:  jamzhuston@gmail.com
# Description:
# This is a simple calculator project
# the calculator will add, multiply, divide, and subtract

answer = input("Would you like to use the calculator? [Y/N]")

if (answer.lower == "N"):
    sys.exit()

operation = ""
while operation.lower() != "q":
    operation = str(input("""Enter the operation you would like to perform:
                            \nMultiplication --> [*]
                            \nDivision --------> [/]
                            \nSubtraction -----> [-]
                            \nAddition --------> [+]
                            \nOr Quit ---------> [q]"""))
    if operation.lower() == "q":
        print("Thank you for using the calculator")
        break
    num1 = float(input("Enter the first number:  "))
    num2 = float(input("Enter the second number: "))
    match operation:
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case "-":
            print(num1 - num2)
        case "+":
            print(num1 + num2)
        case _:
            print("Thats not an operation")
