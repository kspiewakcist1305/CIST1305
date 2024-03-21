# Design a program that asks the user to enter 10 golf scores. The program should then store the scores in a list and display the scores sorted from lowest to highest.

def main():
    # Create an empty list to store the golf scores
    golf_scores = [] # Create an empty list to store the golf scores

    # Get the golf scores from the user
    for i in range(10): # Loop 10 times
        score = float(input('Enter the golf score: ')) # Get a score from the user  
        golf_scores.append(score) # Add the score to the list

    # Sort the scores
    golf_scores.sort() # Sort the list of scores

    # Display the sorted scores
    print('Here are the sorted scores:') # Display a message
    for score in golf_scores: # Loop through the list of scores
        print(score) # Display the current score


# Call the main function
if __name__ == "__main__":
    main()
