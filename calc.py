
def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("Choose an option:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (×)")
        print("4. Divide (÷)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    calculator()
