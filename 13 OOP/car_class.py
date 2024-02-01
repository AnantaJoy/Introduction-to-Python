class Car:
    def __init__(self, brand, color, mileage, capacity, price):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.capacity = capacity
        self.price = price

    # Getter
    def get_brand(self):
        return self.brand

    # Setter
    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def describe(self):
        print(f"This car is a {self.color} {self.brand} with {self.mileage} miles.")

    def drive(self, miles):
        self.mileage += miles
        print(f"You drove {miles} miles.")

    def fill_tank(self, gallons):
        self.capacity += gallons
        print(f"You filled {gallons} gallons.")

    def get_price(self):
        return f"The price of this car is {self.price}."

    def __str__(self):
        return f"This car class."

    def __repr__(self):
        return f"This car class."


# object instantiation
my_car = Car("Toyota", "red", 1000, 15, 10000)
my_car.describe()
my_car.drive(100)
my_car.fill_tank(10)
my_car.describe()
print(my_car.get_price())
