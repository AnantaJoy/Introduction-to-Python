# zip to objects 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Zip lists into a list of objects
combined_zip = zip(list1, list2)


print(combined_zip)


# print the zip object
print([*combined_zip]) # tuple unpacking
# print(list(combined_zip))