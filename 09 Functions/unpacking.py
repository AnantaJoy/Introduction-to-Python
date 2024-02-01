def main():
    hey(["This", "is", "2024"])


def hey(words):
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()