class Student:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def print_student(self):
        print(f"{self.name} is from {self.dept} department.")

    def __str__(self):
        return f"This is student class. {self.name} is from {self.dept} department."


def main():
    student = Student("John", "EEE")
    print(student)


if __name__ == "__main__":
    main()
