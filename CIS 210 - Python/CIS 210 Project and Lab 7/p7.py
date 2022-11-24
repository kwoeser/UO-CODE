# CIS 210 Winter 2021-2022 Project 7
# Karma Woeser
# Project 7 - Titanic 

import csv
import matplotlib.pyplot as plt
import statistics

def load_data(file_name:str, types:dict) -> dict:
    '''Opens and reads a csv file and creates a dictiontary from it.

        Args:
                file_name: name of the file that is going to be read
                types: type of the 
        
        Returns:
                data_dict : a dict of the data inside the file_name
    '''
    with open(file_name, 'r', encoding = 'utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        titles = next(csv_reader)


        data_dict = {Key: [] for Key in tuple(zip(titles, types.values()))}

        #print(data_dict)
        
        for line in csv_reader:
            count = 0
            
            for i, ty in types.items():
                data_dict[(i, ty)].append(ty(line[count]))
                count += 1
                
    
    return data_dict

TITANIC_TYPES = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
data = load_data('Titanic-clean.csv', TITANIC_TYPES)
for key, val in data.items():
    print(key, val[:4])


def summarize(data:dict):
    '''Finds the min, max, mean, stdev, and mode for every column. If the column's values are
    anything but a int or float. It will find the unique values and most common values.

        Args:
                data: a dict of the data inside the file_name
        
        Returns:
                None
    '''
    for keys, values in data.items():
        if isinstance(values[0], str):
            unique = len(set(values))

            counts = {}
            for item in values:
                if item in counts:
                    counts[item] += 1
                else:
                    counts[item] =1


            Max = -1
            maxElement = 0
            for key in counts:
                if counts[key] > Max:
                    Max = counts[key]
                    maxElement = key

            
            print('Statistics for {0}:'.format(keys[0]))
            print('Number of unique values:', unique)
            print('\t Most common values:', maxElement)

        else:
            print('Statistics for {0}:'.format(keys[0]))
            print(f'{min.__name__:>7} : {float(round(min(values), 1)):>6}')
            print(f'{max.__name__:>7} : {float(round(max(values), 1)):>6}')
            print(f'{statistics.mean.__name__:>7} : {float(round(statistics.mean(values), 1)):>6}')
            print(f'{statistics.stdev.__name__:>7} : {float(round(statistics.stdev(values), 1)):>6}')
            print(f'{statistics.mode.__name__:>7} : {float(round(statistics.mode(values), 1)):>6}')
            




def pearson_corr(x:list, y:list) -> float:
    '''Finds the pearson correlation between two different columns using the statistics module

        Args:
                data: a dict of the data inside the file_name
        
        Returns:
                corr (float): the correlation between two different columns
    '''
    xBar = statistics.mean(x)
    yBar = statistics.mean(y)
    xStd = statistics.stdev(x)
    yStd = statistics.stdev(y)

    num = 0.0

    for i in range(len(x)):
        num = num +(x[i] - xBar) * (y[i] - yBar)
    corr = num / ((len(x) - 1) * xStd * yStd)
    return round(corr, 2)




def survivor_vis(data:dict, col1:tuple, col2:tuple) -> plt.Figure:
    '''Visualizes the surviovers and deaths on the Titanic, using two differnet columns as
    the x and y

        Args:
                data: a dict of the data inside the file_name
                col1: a key from data
                col2: a key from data
                
        Returns:
                plt.figure: visualizes the graph
    '''
    x_vals = data[col1]
    y_vals = data[col2]
    passe = data[('Survived', int)]

    list_of_x_of_survivors = []
    list_of_y_of_survivors = []
    list_of_x_of_deaths = []
    list_of_y_of_deaths = []
    
    for i in range(len(passe)):
        x = x_vals[i]
        y = y_vals[i]
        survived = passe[i]


        if survived == 1:
            list_of_x_of_survivors.append(x)
            list_of_y_of_survivors.append(y)

        else:
            list_of_x_of_deaths.append(x)
            list_of_y_of_deaths.append(y)
            
    
    # Scatter for surviors
    plt.scatter(list_of_x_of_survivors, list_of_y_of_survivors, marker='o',c='green',label='Survived')
    # Sctter for the deaths
    plt.scatter(list_of_x_of_deaths, list_of_y_of_deaths, marker='+',c='red',label='Died')
    


    plt.title('Survival of Titanic Passengers')
    plt.xlabel(col1[0]) 
    plt.ylabel(col2[0])
    plt.legend()
    #plt.savefig(f'scatter-{col1[0]}-{col2[0]}.png')
    plt.show(block = False)
   





# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 7."""

    # 7.1 Load the dataset
    TITANIC_TYPES = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', TITANIC_TYPES)

    # 7.2 Print informative summaries
    print("\nPart 7.2")
    summarize(data)

    print("\nPart 7.3")
    # 7.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 7.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 7.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 7.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()

