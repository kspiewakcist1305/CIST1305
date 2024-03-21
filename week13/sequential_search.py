def sequential_search(arr, target):
    for i in range(len(arr)): # Loop through the list
        if arr[i] == target: # If the current element is the target
            return i # Return the index of the target
    return -1 # If the target is not found, return -1


def main():
    array = [1,2,3,4,5] # Create a list of numbers
    invalid_input = True # Flag to check if the input is valid

    while invalid_input: # Loop until the user enters a valid input
        try: # Try to get the target from the user
            target = int(input("Please enter the number you are looking for: ")) # Get the target from the user
            invalid_input = False # If the input is valid, set the flag to False
        except: # If the input is not valid
            print("Invalid input please try again dummy!") # Display an error message

    index = sequential_search(array, target) # Search for the target in the list

    if index != -1: # If the target was found
        print('The target was found at index', index) # Display the index of the target
    else: # If the target was not found
        print('The target was not found in the list.') # Display a message indicating the target was not found


# Call the main function
if __name__ == "__main__":
    main()