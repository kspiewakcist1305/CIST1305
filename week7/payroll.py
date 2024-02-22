# Student: Krystian Spiewak
# Date: 02/21/2024
# Program: Payroll

# This program calculates the gross pay for an employee.
# The user enters the hourly pay rate and the number of hours worked.
# The program displays the gross pay.

# Define the main function
def main():
    # Get the hourly pay rate
    pay_rate = float(input('Enter the hourly pay rate: '))
    # Get the number of hours worked
    hours_worked = float(input('Enter the number of hours worked: '))
    # Validate the input
    if pay_rate < 7.50 or pay_rate > 18.25:
        print('Error: The hourly pay rate is invalid.')
    elif hours_worked < 0 or hours_worked > 40:
        print('Error: The number of hours worked is invalid.')
    else:
        # Calculate the gross pay
        gross_pay = pay_rate * hours_worked
        # Display the gross pay
        print('The gross pay is $', format(gross_pay, ',.2f'), sep='')


# Call the main function
main()
