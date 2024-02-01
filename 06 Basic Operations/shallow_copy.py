# shallow copy 

original = [1,2,3,4,5]
shallow_copy = original
shallow_copy[3] = 20
print(original)
print(shallow_copy)

# id() function returns the identity of an object
print(id(original))
print(id(shallow_copy))