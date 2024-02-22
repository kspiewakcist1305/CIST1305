# Student Name: Krystian Spiewak
## Lab10-1/Chapter7 Debugging

### 1 - Issue with program that validates user input in range 1 to 10
The issue with the program is that the condition in the while loop is incorrect, it is using he incorrect operator `AND` instead of the correct one in this case `OR`. This program would enter an infinite loop as the value cannot be simultaneously smaller than 1 AND greater than 10. Correct code:
``` VB
...
While value < 1 OR value > 10
...
```

### 2 - Issue with program that gets a dollar amount from user.
The issue with the program is that the program does not get a different input from the user if they enter a value that is less than 0. This would cause an infinite loop. Correct program:
``` VB
...
While amount < 0
    Display "ERROR: ..."
    Display "Enter a dollar amount."
    Input amount
...
```

### 3 - Issue with program that asks the user to enter a string.
The issue with the program is that the user needs to pay attention to capitalization when entering the string. The correct program:
``` VB
...
While toLower(choice) != "lisa" AND toLower(choice) != "tim"
...
```
