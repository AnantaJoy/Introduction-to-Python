import sys

print("Hello", sys.argv[0])
# print("You entered", sys.argv[1])

for arg in sys.argv:
    print(arg)