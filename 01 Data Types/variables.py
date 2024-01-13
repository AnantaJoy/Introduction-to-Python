# Variables are used to store information to be referenced and manipulated in a computer program.
# They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves.

fruits = "Mango"
print(fruits)

# Variable naming conventions:
# 1. Variables names must start with a letter or an underscore.
# 2. The remainder of your variable name may consist of letters, numbers and underscores.
# 3. Names are case sensitive.
# 4. Avoid using Python built-in keywords like int and str as variable names.
# 5. Use a name that describes the kind of information that is stored in the variable.

# Variable name examples:
myName = "John"
my_age = 20
my_age2 = 20.5
my_age3 = 20 + 5j
_my_age = 20
_location1 = "Dhaka"
print(id(myName))
print(id(my_age))

# id return the memory address of the variable
# print(id(myName)) # 140133731366864

# InValid variable name examples:
# 1myName = "John"
# my-name = "John"
# my name = "John"
# my@name = "John"
# my#name = "John"
# my$name = "John"
