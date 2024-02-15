# Name: Krystian Spiewak
# This program is going to roll two dice and print the result.

# Importing the required libraries
import random


# Defining the main function
def main():
    # Printing the welcome message
    print("Welcome to the Dice Roller!")
    print("This program will roll two dice and print the result.")

    # Rolling the dice
    roll_dice()

    # Asking the user if they want to roll again
    roll_again = input("Do you want to roll again? (yes/no): ")

    # Checking the user's response
    if roll_again.lower() == "yes":
        main()
    elif roll_again.lower() == "no":
        print("Thank you for using the Dice Roller!")
    else:
        print("Invalid response! Please try again.")
        main()


# Defining the roll dice function
def roll_dice():
    # Rolling the first die
    die1 = random.randint(1, 6)

    # Rolling the second die
    die2 = random.randint(1, 6)

    # Printing the result
    print("The first die rolled", die1)
    print("The second die rolled", die2)
    print("The total is", die1 + die2)


# Calling the main function
main()
