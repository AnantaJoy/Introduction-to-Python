# Global variables
a = 1
b = 2


def foo():
    # local variables
    a = 3
    b = 4
    print(a)
    print(b)


foo()
print(a)
print(b)

# making a a local variable to global variable

a = 1
b = 2


def sum():
    global c
    a = 3
    b = 4
    c = a + b


sum()
print(c)
