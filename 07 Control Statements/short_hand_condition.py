# Shorthand if-elif-else condition
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)

x = 15
result2 = "Even" if x % 2 == 0 else ("Zero" if x == 0 else "Odd")
print(result2)