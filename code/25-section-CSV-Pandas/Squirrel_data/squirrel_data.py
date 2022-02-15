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

#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
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
# data_dict = {
#     "students": ["Amy", "James", "Angle"],
#     "scores": [75, 56, 65]
# }
#
# data_from_dict = pandas.DataFrame(data_dict)
# print(data_from_dict)
# data.to_csv("new_data.csv")
#
# data_from_dict.to_excel("data_check.xlsx")


# using Central Park Squirrel Data
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


