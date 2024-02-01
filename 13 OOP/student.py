def main():
    name = get_name()
    age = get_age()
    print(f"Hello {name}, you are {age} years old.", end="")


def get_name():
    return input("Enter your name: ")


def get_age():
    return input("Enter your age: ")


if __name__ == "__main__":
    main()
