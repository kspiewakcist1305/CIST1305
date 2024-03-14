class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

classroom = [Student("Bob", 32), Student("Suzan", 21)]

def main():
    # s1 = Student("John", 36)
    print("BEFORE")
    for s in classroom:
        print_student(s)
        
    add_student()

    print("AFTER")
    for s in classroom:
        print_student(s)


def add_student():
    name = input("Please input student name: ")
    age = input("Please input student age: ")
    classroom.append(Student(name, age))

    


def print_student(s: Student):
    print(f'Student name is: {s.name}')
    print(f'Student age is: {s.age}')


if __name__ == "__main__":
    main()
