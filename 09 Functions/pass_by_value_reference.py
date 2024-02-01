# pass by value


def change_value(num):
    num = 100


n = 5
change_value(n)
print(n)  # Outputs: 5


# pass by reference
def change_value(lst):
    lst[0] = 100


my_list = [1, 2, 3]
change_value(my_list)
print(my_list)  # Outputs: [100, 2, 3]
