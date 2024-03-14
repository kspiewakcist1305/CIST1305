CARS = ["Buick", "Ford", "Fiat", "Toyota"]


def promptForNewCar(arr: list) -> list:
    car = input("Add another car: ")
    arr.append(car)


def main():
    print(CARS)
    promptForNewCar(CARS)
    print(CARS)

if __name__ == "__main__":
    main()
    