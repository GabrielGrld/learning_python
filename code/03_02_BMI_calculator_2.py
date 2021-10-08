height = input ("please enter your height in m: ")
weight = input ("please enter your weight in kg: ")

bmi = float(weight)/(float(height)**2)
rounded_bmi = round(bmi, 2)
if rounded_bmi<18.5:
    print (f"your BMI is {rounded_bmi}, you are underweight")

elif rounded_bmi>18.5 and rounded_bmi<25:
    print(f"your BMI is {rounded_bmi}, you are normal weight")
elif rounded_bmi>25 and rounded_bmi<30:
    print(f"your BMI is {rounded_bmi}, you are overweight")
elif rounded_bmi > 30 and rounded_bmi < 35:
    print(f"your BMI is {rounded_bmi}, you are obese")
elif rounded_bmi > 35 and rounded_bmi < 35:
    print(f"your BMI is {rounded_bmi}, you are obese")
