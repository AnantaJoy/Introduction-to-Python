import random
from random import randint, choice
from random import *

# random module provides functions that generate random numbers
print(random.random())

print(random.uniform(1, 10))

print(random.randint(1, 10))

print(random.choice(['apple', 'banana', 'cherry']))

print(random.choices(['apple', 'banana', 'cherry'], k=2))


