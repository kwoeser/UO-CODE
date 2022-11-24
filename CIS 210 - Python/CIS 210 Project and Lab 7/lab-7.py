# CIS 210 Winter 2021-2022 Lab 7
# Karma Woeser
# Lab 7 - Csv and plt Lab


import csv
import matplotlib.pyplot as plt

with open('city-scores.csv', 'r') as csvfile:
    r = csv.reader(csvfile)

    
    data_dict = {}

    
    for i, line in enumerate(r):
        if i > 0:
            key = (line[0], line[1])
            value = {
                'Housing': float(line[3]),
                'Cost_Of_Living': float(line[4]),
                'Commute': float(line[5]),
                'Safety': float(line[6]),
                'Healthcare': float(line[7]),
                'Education': float(line[8])
            }
            data_dict[key] = value


print(data_dict)


def create_total_score(data_dict:dict) -> None:
    ''' Creates new key and value for the dict

    Args:
            data_dict: the dictionary storing all the values

    Returns:
            None
    '''
    for city, scores in data_dict.items():
        total_score = sum(scores.values())
        data_dict[city]['total_score'] = total_score


# In place
create_total_score(data_dict)
#print(data_dict)

# Not inplace
#data_dict = create_total_score(data_dict)

'''
a = [0,5,6,2,6,9]
print(a)

a = sorted(a)
print(a)
'''


cities_scores = [(city, scores['total_score']) for city, scores in data_dict.items()]


cities_scores = sorted(cities_scores, key = lambda x: x[1], reverse = True)

'''
for city, score in cities_scores[:10]:
    print(city,score)
'''


housing_cost_scores = [
    (values['Housing'], values['Cost_Of_Living'])
    for values in data_dict.values()
]


housing_scores, cost_of_living_scores = zip(*housing_cost_scores)

#housing_scores = [x[0] for x in housing_cost_scores]
#cost_of_living_scores = [x[1] for x in housing_cost_scores]

plt.scatter(housing_scores, cost_of_living_scores , marker = '+')
plt.title('Housing scores vs Cost of Living')
plt.xlabel('Housing')
plt.ylabel('Cost of living')

plt.show()



