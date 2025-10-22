# Terminal Calculator

import math

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return  a / b

def modulo(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return  a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial not defined for negative number!"
    return  math.factorial(a)

def show_menu():
    print("\n=== Calculator Menu === ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. power (**)")
    print("7. square_root ()")
    print("8. factorial (x!)")
    print("9. View History ")
    print("0. Exit ")
    print("=====================================")

def main():
    while True:
        show_menu()
        choice = input("Select an operation (0-9):  ")

        if choice == "0":
            print("\nThank you for using the calculator. Goodbye")
            break

        elif choice == "9":
            if history:
                print("\n--- Calculation History:")
                for record in history:
                    print(record)
            else:
                print("\nNo calculation yet")
            continue

        elif choice in ["7", "8"]:
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number. ")
                continue

            if choice == "7":
                result = square_root(num)
                expression = f"{num} = {result}"
            elif choice == "8":
                result = factorial(int(num))
                expression = f"{int(num)}! = {result}"

        elif choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! please enter valid numbers. ")
                continue

            if choice == '1':
                result = add(a, b)
                expression = f"{a} + {b} = {result}"
            elif choice == '2':
                result = subtract(a, b)
                expression = f"{a} - {b} = {result}"
            elif choice == '3':
                result = multiply(a, b)
                expression = f"{a} * {b} = {result}"
            elif choice == '4':
                result = divide(a, b)
                expression = f"{a} / {b} = {result}"
            elif choice == '5':
                result = modulo(a, b)
                expression = f"{a} % {b} = {result}"
            elif choice == '6':
                result = power(a, b)
                expression = f"{a}^{b} = {result}"
        else:
            print("Invalid choice! Please select a valid option.")
            continue

        print(f"\nResult: {result}")
        history.append(expression)

if __name__ == "__main__":
    main()








