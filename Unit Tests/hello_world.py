def main():
    name = input("What is your name? ")
    print(hello(name))


def hello(name="World"):
    return "Hello, {}!".format(name)


if __name__ == "__main__":
    main()
