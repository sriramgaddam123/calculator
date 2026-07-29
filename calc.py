
import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator():
    while True:
        print("\n--- Command-Line Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Clear Screen")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '6':
            print("Exiting calculator... Goodbye!")
            break
        elif choice == '5':
            clear_screen()
            continue

        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} × {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} ÷ {num2} = {result}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    calculator()
