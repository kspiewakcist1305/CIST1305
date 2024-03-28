while True:
    q = input("Add(a) or Search(s) or Quit(q): ")
    if q == "a":
        with open("contact.txt", 'a') as f:
            name = input("Name: ")
            phone_number = input("Phone: ")
            email = input("Email: ")
            f.writelines(('Name: ', name, '\n', 'Phone: ', phone_number, '\n', 'Email: ', email, '\n\n'))
    elif q == "s":
        with open("contact.txt", "r") as f:
            search = input("Search: ")
            for line in f:
                if search in line:
                    print(line)
    else:
        break
    