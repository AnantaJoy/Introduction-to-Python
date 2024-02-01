student_info = [
    {"name": "John", "age": 21, "gpa": 3.45, "year": "Senior"},
    {"name": "Jane", "age": 20, "gpa": 3.25, "year": "Junior"},
    {"name": "Bob", "age": 19, "gpa": 3.75, "year": "Sophomore"},
    {"name": "Mike", "age": 22, "gpa": 3.15, "year": "Senior"},
    {"name": "Jill", "age": 21, "gpa": 3.65, "year": "Junior"},
    {"name": "Jack", "age": 20, "gpa": 3.05, "year": "Sophomore"},
    {"name": "Bill", "age": 19, "gpa": 3.95, "year": "Freshman"},
]

cgpa = []
for student in student_info:
    if student["year"] == "Senior":
        cgpa.append(student["gpa"])

print(cgpa)

names = []
for student in student_info:
    if student["name"] not in names:
        names.append(student["name"])

print(names)

ages = []
for student in student_info:
    if student["age"] >= 20:
        ages.append((student["age"], student["year"]))

print(ages)


if __name__ == "__main__":
    pass