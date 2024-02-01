try:
    # Trying to access a variable that doesn't exist
    print(name)
except NameError:
    # Handling the NameError by printing a custom error message
    print("Variable does not exist!")

