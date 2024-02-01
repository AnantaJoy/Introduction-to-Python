with open("names2.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")

with open("names.txt", "r") as file:
    for line in file:
        print(line, end="")
