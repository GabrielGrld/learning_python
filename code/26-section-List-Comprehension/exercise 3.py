
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

numbers_one = [int(number) for number in file1]
numbers_two = [int(number) for number in file2]

print(numbers_one)
print(numbers_two)
# Write your code above 👆

result = [n1 for n1 in numbers_one if n1 in numbers_two]
print(result)
