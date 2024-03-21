# Tic tac toe game


def print_board():
    for i in range(2):
        for j in range(2):
            print(" |", end=' ')
        
        print()
        print("------")
    for i in range(2):
        print(" |", end=' ') 


def main():
    print_board()


if __name__ == "__main__":
    main()
