# defining a function
def sayHi(name):
    print("Hi", name)
    print("Welcome to Python")


# calling a function
sayHi("John")


# arguments and parameters
def hello(name, age):
    print("Hello", name, "you are", age, "years old")


hello("John", 25)

# Explantion of the above code:
# The function hello() takes two parameters: name and age.
# When we call the function, we pass two arguments: 'John' and 25.
# The function prints the arguments in the print statement.


# default parameters
def hello2(name="John", age=25):
    print("Hello", name, "you are", age, "years old")


hello2()

# Explantion of the above code:
# The function hello2() takes two parameters: name and age.
# When we call the function, we pass no arguments.
# The function prints the default parameters in the print statement.


# returning values
def add(x, y):
    return x + y


print(add(5, 3))
