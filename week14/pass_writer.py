# password = input("create a password? ")
def view():
    print("\nYour stored passwords are: \n")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            user, password = line.split(" | ")
            print(f"Account: {user} Password: {password}")


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # with allows our code to auto close
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
