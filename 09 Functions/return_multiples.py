def student_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age


def main():
    name, age = student_info()
    print(f"Hello {name}, you are {age} years old.", end="")


if __name__ == "__main__":
    main()
