MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def daysOfMonth(month, year):
    month = month.lower()
    if month == "february":
        if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
            return 29
        else:
            return 28
    elif month in ["april", "june", "september", "november"]:
        return 30
    else:
        return 31


def main():
    days = []
    year = int(input("Please enter the year: "))
    print(f"In the year {year}: ")
    for i in range(12):
        days.append(daysOfMonth(MONTHS[i], year))
    for i in range(12):
        print(MONTHS[i], "has", days[i], "days.")


if __name__ == "__main__":
    main()
