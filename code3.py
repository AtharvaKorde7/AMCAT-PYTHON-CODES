import sys

def addition(num1, num2):
    print("Addition =", num1 + num2)

def subtraction(num1, num2):
    print("Subtraction =", num1 - num2)

def multiplication(num1, num2):
    print("Multiplication =", num1 * num2)

def division(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Division =", num1 / num2)

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice from above option (1-5): "))

    if choice == 5:
        print("Exiting the program.")
        sys.exit()

    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))

    if choice == 1:
        addition(val1, val2)
    elif choice == 2:
        subtraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        division(val1, val2)
    else:
        print("Invalid choice. Please try again.")