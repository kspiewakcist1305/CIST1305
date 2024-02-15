# This program will be an advanced calculator that can perform the following operations:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Exponential function
# 7. Factorial
# 8. Square Root
# 9. Logarithm
# 10. Exit

# Importing the required libraries
import math


# Defining the main function
def main():
    # Printing the welcome message
    print("Welcome to the Calculator!")
    print("This program can perform the following operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Factorial")
    print("7. Square Root")
    print("8. Logarithm")
    print("9. Exit")

    # Getting the user's choice
    choice = int(input("Please enter your choice: "))

    # Performing the selected operation
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        exponentiate()
    elif choice == 6:
        factorial()
    elif choice == 7:
        square_root()
    elif choice == 8:
        logarithm()
    elif choice == 9:
        exit()
    else:
        print("Invalid choice! Please try again.")
        main()


# Defining the add function
def add():
    # Getting the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the addition
    result = num1 + num2

    # Displaying the result
    print("The sum of", num1, "and", num2, "is", result)

    # Asking the user if they want to perform another operation
    another_operation()


# Defining the subtract function
def subtract():
    # Getting the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the subtraction
    result = num1 - num2

    # Displaying the result
    print("The difference between", num1, "and", num2, "is", result)

    # Asking the user if they want to perform another operation
    another_operation()


# Defining the multiply function
def multiply():
    # Getting the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the multiplication
    result = num1 * num2

    # Displaying the result
    print("The product of", num1, "and", num2, "is", result)

    # Asking the user if they want to perform another operation
    another_operation() 


# Defining the divide function
def divide():
    # Getting the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the division
    result = num1 / num2

    # Displaying the result
    print("The quotient of", num1, "and", num2, "is", result)

    # Asking the user if they want to perform another operation
    another_operation() 


# Defining the exponentiate function
def exponentiate():
    # Getting the numbers from the user
    num1 = float(input("Enter the base: "))
    num2 = float(input("Enter the exponent: "))

    # Performing the exponentiation
    result = num1 ** num2

    # Displaying the result
    print(num1, "raised to the power of", num2, "is", result)

    # Asking the user if they want to perform another operation
    another_operation()


# Defining the factorial function
def factorial():
    # Getting the number from the user
    num = int(input("Enter the number: "))

    # Performing the factorial
    result = math.factorial(num)

    # Displaying the result
    print("The factorial of", num, "is", result)

    # Asking the user if they want to perform another operation
    another_operation()


# Defining the square root function
def square_root():
    # Getting the number from the user
    num = float(input("Enter the number: "))

    # Performing the square root
    if num < 0:
        print("Invalid input")
    else:
        result = num ** 0.5
        print("The square root of", num, "is", result)

    # Asking the user if they want to perform another operation
    another_operation() 


# Defining the logarithm function
def logarithm():
    # Getting the number and base from the user
    num = float(input("Enter the number: "))
    base = float(input("Enter the base: "))

    # Performing the logarithm
    result = math.log(num, base)

    # Displaying the result
    print("The logarithm of", num, "to the base", base, "is", result)

    # Asking the user if they want to perform another operation
    another_operation()


# Defining the exit function
def exit():
    # Printing the exit message
    print("Thank you for using the Calculator!")
    print("Goodbye!")

    # Exiting the program
    quit()


# Defining the another operation function
def another_operation():
    # Asking the user if they want to perform another operation
    another = input("Do you want to perform another operation? (yes/no): ")

    # Checking the user's choice
    if another == "yes":
        main()
    elif another == "no":
        exit()
    else:
        print("Invalid choice! Please try again.")
        another_operation()
    

# Calling the main function
main()
