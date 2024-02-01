name = input("Enter your name: ")

with open("names2.txt", "a") as f:
    f.write(name + "\n")
