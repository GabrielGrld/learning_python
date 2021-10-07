print ("Welcome to the tip calculator")
total_bill = float(input ("What was the total bill\n"))
people = int(input("How many people to split the bill? \n"))
tip_percentage = float(input("What percentaje tip would you like to give? 10, 12 or 15? "))
pay_per_person = (total_bill*(tip_percentage/100+1))/people
final_amount = round(pay_per_person, 2)
print (f"Each person should pay  ${final_amount}")
