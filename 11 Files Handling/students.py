import csv

name = input("Enter name: ")
age = input("Enter age: ")
course = input("Enter course: ")

with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow((name, age, course))
    writer = csv.DictWriter(file, fieldnames=["name", "age", "course"])
    writer.writerow({"name": name, "age": age, "course": course})

if __name__ == "__main__":
    pass
