class Phonebook:

    def __init__(self):
        self.data = {}

    def add(self, name, number):
        self.data[name] = number

    def lookup(self, name):
        return self.data.get(name)

    def names(self):
        return list(self.data.keys())
    
    def numbers(self):
        return list(self.data.values())
    