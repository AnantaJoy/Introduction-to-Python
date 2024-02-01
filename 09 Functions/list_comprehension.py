def main():
    hey(["This", "is", "2024"])


def hey(words):
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    # uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
