# using thrird variable
x = 10
y = 20
print(f"x = {x}, y = {y}")
temp = x
x = y
y = temp
print(f"x = {x}, y = {y}")

# without using third variable
x = 10
y = 20
print(f"x = {x}, y = {y}")
x = x + y
y = x - y
x = x - y
print(f"x = {x}, y = {y}")

# using pythonic way(tuple unpacking)
x = 10
y = 20
print(f"x = {x}, y = {y}")
x, y = y, x
print(f"x = {x}, y = {y}")

# using xor
x = 10
y = 20
print(f"x = {x}, y = {y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"x = {x}, y = {y}")

# using arithmetic
x = 10
y = 20
print(f"x = {x}, y = {y}")
x = x * y
y = x // y
x = x // y
print(f"x = {x}, y = {y}")