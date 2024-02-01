# calculaate the bmi
# bmi = weight / (height * height)
# bmi < 18.5 - underweight
# 18.5 <= bmi < 25 - normal
# 25 <= bmi < 30 - overweight
# bmi >= 30 - obese

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight / (height * height)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are normal")
elif 25 <= bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
    

# if elif else
# if condition:
#     statements
# elif condition:
#     statements
# ...
# ...
# else:
#     statements
