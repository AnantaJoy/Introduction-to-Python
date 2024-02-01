# print("Hello World) 
# Output: SyntaxError

num = int(input("Enter a number:")) # Goes Wrong when input is not a number

print(f"The number is {num}")

try:
    num = int(input("Enter a number:"))
    print(f"The number is {num}")
except ValueError:
    print("The number is not a integer number")

try:
    num = int(input("Enter a number:"))
    print(f"The number is {num}")
except Exception as e:
    print(e)
