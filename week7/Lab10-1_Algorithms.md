# Student Name: Krystian Spiewak
## Lab10-1/Chapter7 Algorithms

### 1 - Algorithm that prompts the user to enter a positive nonzero number.
``` VB
Declare Real number = 0
While number < 1
    Display "Please enter a positive, nonzero number: "
    Input number
End While
Display "Thank you!"
```

### 2 - Algorithm that prompts user to enter a number in range of 1 to 100
``` VB
Declare Real number = 0
While number < 1 OR number number > 100
    Display "Please enter a number in range 1 to 100: "
    Input number
End While
Display "Thank you!"
```

### 3 - Algorithm that prompts the user to enter "yes" or "no"
``` VB
Declare String answer = ""
While toLower(answer) != "yes" OR toLower(answer) != "no"
    Display "Please enter 'yes' or 'no': "
    Input answer
End While
Display "Thank you!"
```

### 4 - Algorithm that prompts the user to enter a number that is greater than 99.
``` VB
Declare Real number = 0
While number > 99
    Display "Please enter a number that is greater than 99: "
    Input number
End While
Display "Thank you!"
```

### 5 - Algorithm that prompts the user to enter a secret word that is at least 8 characters long.
``` VB
Declare String secret = ""
While length(secret) < 8
    Display "Please enter a secret word that is at least 8 characters long: "
    Input secret
End While
Display "Thank you!"
```
