def create_3d_list_1(x, y, z):
    lst = []
    for i in range(x):
        lst_2d = []
        for j in range(y):
            lst_1d = []
            for k in range(z):
                lst_1d.append('#')
            lst_2d.append(lst_1d)
        lst.append(lst_2d)
    return lst


def main():
    # x = int(input("Please enter 1: "))
    # y = int(input("Please enter 2: "))
    # z = int(input("Please enter 3: "))

    output_1 = create_3d_list_1(1, 3, 3)
    for board in output_1:
        for row in board:
            print(row)


if __name__ == "__main__":
    main()