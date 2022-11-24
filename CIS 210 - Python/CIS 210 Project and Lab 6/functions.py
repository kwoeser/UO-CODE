# CIS 210 Winter 2021-2022 Lab 6
# Karma Woeser
# Lab 6 - Functions

filename = 'november_rain.csv'
with open(filename, 'r') as f:
    lines = f.readlines()


# List comprehension 
data_list = [x.strip().split(',') for x in lines]

print(lines)

# Dictionary comprehension
data_dict = {int(ym): float(rf) for ym, rf in data_list}   


#rainfall_values = data_dict.values()
rainfall_values = [v for k,v in data_dict.items()]

mean_rainnfall = sum(rainfall_values) / len(rainfall_values)
print(data_dict)
print(mean_rainnfall)



yms = [k for k,v in data_dict.items()]
yms = sorted(yms)
ys = [k//100 for k in yms]
values = [data_dict[ym] for ym in yms]
averages = [mean_rainnfall] * len(ys)

import matplotlib.pyplot as plt 

plt.plot(ys, values, 'rx')
plt.plot(ys, averages, 'b')
plt.show()

high_rain_years = [
    ym
    for ym, rf in data_dict.items()
    if rf >= 1.5 * mean_rainfall
]

with open('out.txt', 'w') as f:
    for ym in high_rain_years:
        rf = data_dict[ym]
        f.write(f'Year: {ym//100}, Average rainfall in Inches: {rf}, Percentage increase: {(rf-mean_rainfall)/mean_rainfall*100.0}%\n ')
