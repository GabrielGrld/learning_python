# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
# print(data_dict["temp"])
# temp_list = data["temp"].to_list()
# mean_series = data["temp"].mean()
# print(mean_series)
# print(sum(temp_list)/len(temp_list))
# print(f"Max Temp value is: {data['temp'].max()}")


# Get Data in Row
# This can be useful if we need ot filter something, in this case, we filter the days that are equal to Monday
# in the second print we are filtering the max value in the dataset, using the function max()

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp*(9/5)+32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angle"],
    "scores": [75, 56, 65]
}

data_from_dict = pandas.DataFrame(data_dict)
print(data_from_dict)
data.to_csv("new_data.csv")

data_from_dict.to_excel("data_check.xlsx")
