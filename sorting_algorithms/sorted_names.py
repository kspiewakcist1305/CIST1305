# Design a program that asks the user to enter 20 names into a list. The program should then store the names in a list and display the names sorted from lowest to highest.

def main():
    # Create an empty list to store the names
    names = [] # Create an empty list to store the names

    # Get the names from the user
    for i in range(20): # Loop 20 times
        name = input('Enter a name: ') # Get a name from the user
        names.append(name) # Add the name to the list

    # Sort the names
    names.sort() # Sort the list of names

    # Display the sorted names
    print('Here are the sorted names:') # Display a message
    for name in names: # Loop through the list of names 
        print(name) # Display the current name


# Call the main function
if __name__ == "__main__":
    main()
