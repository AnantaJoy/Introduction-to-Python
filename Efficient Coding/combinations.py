# combinations of list items using itertools
import itertools

# Define the list
my_list = [1, 2, 3, 4, 5]

# Iterate over the list
for item in itertools.combinations(my_list, 2):
    print(item)

# Iterate over the list
print(list(itertools.combinations(my_list, 2)))

# Iterate over the list
print(list(itertools.combinations(my_list, 3)))