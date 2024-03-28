# Name: Krystian Spiewak
# Date: 03/27/2024

contact_book = {}


def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = [phone_number, email]


def display_contacts():
    print(f"\tNAME\t\t\tPHONE NUMBER\t\t\tEMAIL")
    for name, contact in contact_book.items():
        print(f"\t{name}\t\t\t{contact[0]}\t\t\t{contact[1]}")


def search_contact():
    s = input("Enter the name to search: ")
    if s in contact_book:
        contact = contact_book[s]
        print(f"Name: {s}, Phone: {contact[0]}, Email: {contact[1]}")
    else:
        print("Name not found")
        

def main():
    while True:
        add_contact()
        if input("Do you want to add more contacts? (y/n): ") == "n":
            break
    display_contacts()
    search_contact()


if __name__ == "__main__":
    main()
