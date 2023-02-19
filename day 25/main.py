#with open("day 25/weather_data.csv") as file:
#    print(file.readlines())

import csv


with open("day 25/weather_data.csv") as data_file:
    data = csv.reader(data_file) # obiekt
    temperatures = []
    for row in list(data)[1:]:
        print(row) # row jest traktowany jako lista
        temperatures.append(row[1])

print(temperatures)

