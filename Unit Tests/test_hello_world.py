from hello_world import hello


def main():
    test_hello()


def test_hello():
    assert hello() == "Hello, World!"
    assert hello("Python") == "Hello, Python!"
    assert hello("Monty") == "Hello, Monty!"


if __name__ == "__main__":
    main()
