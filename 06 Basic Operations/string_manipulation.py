# Strings are collections of characters. They are immutable.
# Strings can be indexed and sliced like lists.
# Strings can be concatenated using the + operator.
# Strings can be repeated using the * operator.
# Strings can be split using the split() method.
# Strings can be joined using the join() method.
# Strings can be formatted using the format() method.
# Strings can be formatted using f-strings.

# 07. String Manipulation

country = "Bangladesh"
print(country[0])
print(country[-1])
print(country[0:4])
print(country[4:])
print(country[:4])

# Strings are immutable
# country[0] = "b" # TypeError: 'str' object does not support item assignment

# Strings can be concatenated using the + operator
name = "Dhaka"
message = "Welcome to " + name
print(message)

# Strings can be repeated using the * operator
message = "Welcome to " + name + " "
print(message * 5)

# Strings can be split using the split() method
message = "Welcome to Dhaka"
print(message.split())

# Strings can be joined using the join() method
message = ["Welcome", "to", "Dhaka"]
print(" ".join(message))

# Strings can be formatted using the format() method
name = "Dhaka"
message = "Welcome to {}".format(name)
print(message)

# Strings can be formatted using f-strings
name = "Dhaka"
message = f"Welcome to {name}"
print(message)

# Strings can be capitalized using the capitalize() method
name = "dhaka"
print(name.capitalize())

# Strings can be uppercased using the upper() method
name = "dhaka"
print(name.upper())

# Strings can be lowercased using the lower() method
name = "DHAKA"
print(name.lower())

print(dir(str))