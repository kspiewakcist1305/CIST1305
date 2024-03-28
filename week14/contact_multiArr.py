names = []
phone_numbers = []

num = 3

for i in range(num):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    names.append(name)
    phone_numbers.append(phone_number)


print(f"\tNAME\t\t\tPHONE NUMBER")

for i in range(num):
    print(f"\t{names[i]}\t\t\t{phone_numbers[i]}")

s = input("Enter the name to search: ")

if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]
    print(f"Name: {name}, Phone: {phone_number}")
else:
    print("Name not found")
