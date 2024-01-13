# deep copy of the original

original = [1, 2, 3, 4, 5]
copy = original.copy()
copy[4] = 50

print(original)
print(copy)

print(id(original))
print(id(copy))

import copy

