# CIS 210 Winter 2021-2022 Project 6
# Karma Woeser
# Project 6 - Earthquakes
# References: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

import csv
import matplotlib.pyplot as plt

def load_data(file_name: str) -> list:
    '''Opens and reads a file using the csv module and creates a list of it

        Args:
                file_name: name of the file that is going to be read
        
        Returns:
                lst: a list of the data inside the file_name
    '''
    lst = []

    csv_file = open(file_name, 'r', encoding = 'utf8')
    csv_reader = csv.DictReader(csv_file)
        
    for line in csv_reader:
        lst.append(line)
    return lst




def get_series(raw_data:list, col_name:str, col_type:type) -> list:
    '''Returns correct column values from the list created in the load_data func

        Args:
                raw_data: the list from the load_data func
                col_name: the name fo the column
                col_type: the type o

        Returns:
                lst: list of values from the load_data func list 

    >>> get_series([], '', int) 
    []
 
    >>> get_series([{'key1': 1.2, 'key2': 3.1}, {'key1': 2.1, 'key2': 4.9}], 'key2', float) 
    [3.1, 4.9]
    '''
    lst = []

    for ea in raw_data:
        lst.append(col_type(ea[col_name]))
    return lst
            


def get_categories(data:list,print_table=True) -> dict:
    '''Prints the amount of

        Args:
                data: list of the earthquake mag values
                print_table: if True runs if False just prints result of dictionary

        Returns:
                dictionary: new dictionary created with data from previous list
                
    >>> get_categories([4.5, 5.6, 4.6, 6.5, 6.7, 7.9, 8.6, 4.7, 9.2, 9.6, 7]) 
    Light     : 3 
    Moderate  : 1 
    Major     : 2 
    Strong    : 5 
    {'light': 3, 'moderate': 1, 'major': 2, 'strong': 5} 
 
    >>> get_categories([], False)
    Light     : 0
    Moderate  : 0 
    Major     : 0 
    Strong    : 0 
    {'light': 0, 'moderate': 0, 'major': 0, 'strong': 0} 

    '''
    dictionary = {'light': 0, 'moderate': 0, 'major': 0, 'strong': 0}
    
    for mag in data:
        if 4.5 <= mag and 4.9 >= mag:
            dictionary['light'] += 1
        elif 5 <= mag and 5.9 >= mag:
            dictionary['moderate'] += 1
        elif 6 <= mag and 6.9 >= mag:
            dictionary['major'] += 1
        else:
            dictionary['strong'] += 1
            
    print('Light     :', dictionary.get('light'))
    print('Moderate  :', dictionary.get('moderate'))
    print('Major     :', dictionary.get('major'))
    print('Strong    :', dictionary.get('strong'))
    return dictionary




def plot_bar(x:list, y:list, title:str) -> plt.Figure:
    '''Using the matplotlib module creates an bar graph of earthquakes between 2020 and 2021

        Args:
                x: values from list
                y: valies from list
                title: the title on the top

        returns:
                plt.show(): shows the bar graph
    '''
    plt.title(title)
    plt.bar(x, y, color = ['red'])
    plt.savefig(f'barplot-{title}.png')
    plt.show(block = False)
    return plt.show()



def plot_scatter(x:list, y:list, title:str) -> plt.Figure:
    '''Using the matplotlib module creates an scatter graph of earthquakes between 2020 and 2021

        Args:
                x: values from list
                y: valies from list
                title: the title on the top

        returns:
                plt.show(): shows the scatter graph
    '''
    plt.title(title)
    plt.scatter(x, y, color = ['blue'])
    plt.savefig(f'scatterplot-{title}.png')
    plt.show(block = False)
    return plt.figure()



# --- You shouldn't have to change main()
def main():
    """Perform all required steps for this project by calling other functions.
    """
    # Parts 6.1 and 6.2
    # 2020 data
    eq_data = load_data('earthquakes-2020.csv')
    magnitudes = get_series(eq_data, 'mag', float)
    print("2020 Earthquakes:")
    categories20 = get_categories(magnitudes)

    # 2021 data
    eq_data = load_data('earthquakes-2021.csv')
    magnitudes = get_series(eq_data, 'mag', float)
    print("\n2021 Earthquakes:")
    categories21 = get_categories(magnitudes)

    # Part 6.3
    diff21_20 = []
    for key in categories20.keys():
        diff21_20.append(categories21[key] - categories20[key])

    # Part 6.4
    plot_bar(categories21.keys(), diff21_20, '2021 - 2020 Earthquakes')
    depths = get_series(eq_data, 'depth', float)
    plot_scatter(depths, magnitudes, '2020 Depth vs Magnitude')


if __name__ == '__main__':
    main()

