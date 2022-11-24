# CIS 210 Winter 2021-2022 Lab 5
# Karma Woeser
# Lab 5


# Implement your solutions here. Remember to follow 210 Style and PEP8.
# Do not forget to click SUBMIT -- you can submit multiple times without penalty.
#
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run doctests, at the "Console" below, type: python -m doctest p6.py -v
# (if you get an error that p6 cannot be found, click the round arrow "Reset Instance" button in the Console.)
import csv
#import matplotlib.pyplot as plt


def load_data(file_name: str) -> list:
    lst = []
    #with open(file_name, 'r') as csv_file:
    csv_file = open(file_name, 'r', encoding = 'utf8')
    csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            lst.append(dict(line))
    return lst

load_data('earthquakes-2020.csv')

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
