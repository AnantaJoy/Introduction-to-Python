def main():
    hey(["This", "is", "2024"])


def hey(words):
    uppercased = map(str.upper, words)
    print(*uppercased)


def cube(num):
    return num**3


num = [4, 5, 6, 7, 7, 5, 4]
cubed_num = list(map(cube, num))
print(cubed_num)

if __name__ == "__main__":
    main()
