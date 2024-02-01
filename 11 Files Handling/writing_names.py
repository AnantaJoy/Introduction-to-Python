name = input("Enter your name: ")


file = open("names.txt", "w")
file.write(name)
file.close()

with open("names.txt", "w") as f:
    f.write(name)
    f.close()
