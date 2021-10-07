height = input ("please enter your height in m: ")
weight = input ("please enter your weight in kg: ")

bmi = float(weight)/(float(height)**2)
rounded_bmi = round(bmi, 2)
print (f"your BMI is {rounded_bmi}")
