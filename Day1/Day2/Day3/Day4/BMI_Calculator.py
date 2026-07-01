def calculate_bmi(weight,height):
    return (weight / (height * height))

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))


bmi = calculate_bmi(weight,height)

print("BMI : ",round(bmi,2))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
else:
    print("You are overweight")
