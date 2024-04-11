# Creating a menu-based Python program:

import sqlite3
import requests
import os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

db_conn, db_cursor = None, None

MENU = {
    1: "Create user",
    2: "Read users",
    3: "Update user",
    4: "Delete user",
    5: "Exit"
}


def printMenu(menu: dict) -> None:
    for key, option in menu.items():
        print(f'{key}. {option}')
    print('')


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


def useSelection(selection: int) -> None:
    if selection == 1:
        create_user()
    elif selection == 2:
        read_users()
    elif selection == 3:
        update_user()
    elif selection == 4:
        delete_user()
    elif selection == 5:
        print(f'{Fore.CYAN}{Style.DIM}Goodbye!{Style.RESET_ALL}')
        os._exit(0)
    else:
        print('Invalid selection')
        print('')
        printMenu()


def initDB():
    db_conn = sqlite3.connect('week15.sqlite3')
    db_cursor = db_conn.cursor()
    db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    ''')
    return db_conn, db_cursor


def create_user():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    db_cursor.execute('''
    INSERT INTO users (name, email) VALUES (?, ?)
    ''', (name, email))
    db_conn.commit()
    print('User created successfully!')
    print('')


def read_users():
    db_cursor.execute('''
    SELECT * FROM users
    ''')
    users = db_cursor.fetchall()
    for user in users:
        print(user)
    print('')


def update_user():
    user_id = int(input('Enter the user ID: '))
    name = input('Enter the new name: ')
    email = input('Enter the new email: ')
    db_cursor.execute('''
    UPDATE users SET name = ?, email = ? WHERE id = ?
    ''', (name, email, user_id))
    db_conn.commit()
    print('User updated successfully!')
    print('')


def delete_user():
    user_id = int(input(f'{Fore.BLUE}Enter the user ID: {Style.RESET_ALL}'))
    db_cursor.execute('''
    DELETE FROM users WHERE id = ?
    ''', (user_id,))
    db_conn.commit()
    print(f'{Fore.GREEN}User deleted successfully!{Style.RESET_ALL}')
    print('')    



def main():
    global db_conn, db_cursor
    db_conn, db_cursor = initDB()
    while True:
        printMenu(MENU)
        selection = getSelectionInt(MENU.keys())
        useSelection(selection)


if __name__ == '__main__':
    main()


# https://robohash.org/Sheldon.png?set=set4