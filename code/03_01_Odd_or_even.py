number = int(input("Which number do you want to check: \n"))
modulo = number%2
print(f"The modulo is {modulo}")
if modulo == 0:
    print(f"{number} is a even number")
else:
    print (f"{number} is a odd number")