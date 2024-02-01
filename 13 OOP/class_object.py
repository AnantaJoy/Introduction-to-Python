# creating a class
class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age)


# creating an object
obj = UserInfo("John", 25)
obj.details()
