import sqlite3
import datetime

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

db_conn, db_cursor = None, None

MENU = {
    1: 'Buy stock',
    2: 'Sell stock',
    3: 'View portfolio',
    4: 'View transactions',
    5: 'Exit'
}


def printMenu(menu: dict) -> None:
    for key, option in menu.items():
        print(f'{key}. {option}')
    print('')
    print(f'{Fore.BLUE}{Style.DIM}Select an option{Style.RESET_ALL}')


def getSelectionInt(range: list) -> int:
    while True:
        try:
            selection = int(
                input(f'{Fore.YELLOW}Enter your selection: {Style.RESET_ALL}'))
            if selection in range:
                break
        except:
            pass
        print(f'{Fore.RED}Invalid selection{Style.RESET_ALL}')
    return selection


def useSelection(selection: int) -> None:
    match selection:
        case 1:
            buy_stock()
        case 2:
            sell_stock()
        case 3:
            view_portfolio()
        case 4:
            view_transactions()
        case 5:
            print(f'{Fore.CYAN}{Style.DIM}Goodbye!{Style.RESET_ALL}')
            db_conn.close()
            exit(0)
        case _:
            print(f'{Fore.RED}{Style.DIM}Invalid selection{Style.RESET_ALL}')
            print('')
            printMenu(MENU)


def buy_stock():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_type = 'BUY'
    stock_symbol = input('Enter stock symbol: ')
    stock_qty = float(input('Enter quantity: '))
    stock_price = float(input('Enter price: '))
    db_cursor.execute('''
        INSERT INTO stocks (date, trans, symbol, qty, price) 
        VALUES (?, ?, ?, ?, ?)
    ''', date, transaction_type, stock_symbol, stock_qty, stock_price)
    db_conn.commit()
    print(f'{Fore.GREEN}Stock purchased{Style.RESET_ALL}')
    print('')


def sell_stock():
    print('Sell stock')


def view_portfolio():
    print('View portfolio')


def view_transactions():
    print('View transactions')


def initDB():
    db_conn = sqlite3.connect('course_challenge.sqlite3')
    db_cursor = db_conn.cursor()
    db_cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date text,
            trans text,
            symbol text,
            qty real,
            price real
        )
    ''')
    db_conn.commit()
    return db_conn, db_cursor


def main():
    global db_conn, db_cursor
    db_conn, db_cursor = initDB()
    while True:
        printMenu(MENU)
        selection = getSelectionInt(MENU.keys())
        useSelection(selection)


if __name__ == '__main__':
    main()
