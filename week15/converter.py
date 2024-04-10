# Name: Krystian Spiewak
# Date: 4/10/2024
# Converter
# This program has a menu with 3 options: 1. Convert inches to centimeters. 2. Convert feet to meters. 3. Convert miles to kilometers.
# After the user selects the option the program will print out the selection
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

MENU = {
    1: "Convert inches to centimeters",
    2: "Convert feet to meters",
    3: "Convert miles to kilometers",
    4: "Exit"
}

DECIMAL_PLACES = 2


def printMenu(menu: dict) -> None:
    for key, option in menu.items():
        print(f'{key}. {option}')


def getSelectionInt(range: list) -> int:
    while True:
        try:
            selection = int(input("Enter your selection: "))
            if selection in range:
                break
        except:
            pass    
        print("Invalid selection")
    return selection


def getSelectionFloat(prompt: str) -> float:
    while True:
        try:
            selection = float(input(prompt))
            break
        except:
            pass
        print("Invalid selection")
    return selection



def inchesToCentimeters() -> str:
    CONVERSION = 2.54
    inches = getSelectionFloat("Enter the number of inches: ")
    centimeters = round(inches * CONVERSION, DECIMAL_PLACES)
    return f"{inches} inches is equal to {centimeters} centimeters."


def feetToMeters() -> str:
    CONVERSION = 0.3048
    feet = getSelectionFloat("Enter the number of feet: ")
    meters = round(feet * CONVERSION, DECIMAL_PLACES)
    return f"{feet} feet is equal to {meters} meters."


def milesToKilometers() -> str:
    CONVERSION = 1.60934
    miles = getSelectionFloat("Enter the number of miles: ")
    kilometers = round(miles * CONVERSION, DECIMAL_PLACES)
    return f"{miles} miles is equal to {kilometers} kilometers."


def useSelection(selection: int) -> str:
    match selection:
        case 1:
            return inchesToCentimeters()
        case 2:
            return feetToMeters()
        case 3:
            return milesToKilometers()
        case _:
            return ""


def main():
    options = list(MENU.keys())
    selection = 0
    while selection != options[-1]:
        printMenu(MENU)
        selection = getSelectionInt(options)
        result = useSelection(selection)
        if result:
            print(f'{Fore.MAGENTA}Result: {Fore.GREEN}{Style.BRIGHT}{result}{Style.RESET_ALL}')
        print()

    print(f'{Fore.BLUE}{Style.DIM}Thank you for using the program!{Style.RESET_ALL}')


if __name__ == "__main__":
    main()
