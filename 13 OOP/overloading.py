class Car:
    def __init__(self, brand, color, mileage, capacity, price):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.capacity = capacity
        self.price = price

    # other methods...

    def __add__(self, other):
        if isinstance(other, Car):
            return self.mileage + other.mileage
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.mileage - other.mileage
        else:
            raise TypeError("Unsupported operand type for -")


car1 = Car("Toyota", "red", 1000, 15, 10000)
car2 = Car("Honda", "blue", 500, 20, 15000)

total_mileage = car1 + car2
print(total_mileage)  # Output: 1500

difference_mileage = car1 - car2
print(difference_mileage)  # Output: 500
