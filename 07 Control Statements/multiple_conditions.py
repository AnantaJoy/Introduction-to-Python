# we can use multiple conditions in a single if statement
age = int(input("Enter your age: "))
if  age > 18 and age < 65:
    print("You are eligible to work")
else:
    print("You are not eligible to work")
    
    
# if condition1 and condition2 and condition3:

# boolean condition
# or, and, not  
# True, False

# grade calculator
# 80 - 100 -> A+
# 70 - 79 -> A
# 60 - 69 -> B
# 50 - 59 -> C
# 40 - 49 -> D
# 0 - 39 -> F

# 1. take input from user
# 2. check if the input is valid
# 3. calculate grade
marks = int(input("Enter your marks: "))
if marks >= 0 and marks <= 100: # 0 <= marks <= 100:
    if marks >= 80:
        print("A+")
    elif marks >= 70:
        print("A")
    elif marks >= 60:
        print("B")
    elif marks >= 50:
        print("C")
    elif marks >= 40:
        print("D")
    else:
        print("F")

