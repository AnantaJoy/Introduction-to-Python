def main():
    x = int(input("Enter a number: "))
    print("The square of", x, "is", square(x))


def square(x):
    return x * x


if __name__ == "__main__":
    main()
