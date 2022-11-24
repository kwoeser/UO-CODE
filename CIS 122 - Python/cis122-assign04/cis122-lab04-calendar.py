# CIS 122 Fall 2020 Lab 4 Calendar 
# Author: Karma Woeser
# Partner: Your Partner
# References:
# Description: Leap year calendar problem


def get_full_month(month_number):
    '''
    '''
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "Feburay"
    elif month_number == 3:
        return  "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    else:
        print("You must enter an integer between 1 and 12.")
        
def test_get_full_month():
    for i in range(1, 13):
        month = get_full_month(i)
        print(i, month)


test_get_full_month()

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def test_is_leap_year(start_year, end_year):

    for year in range(start_year, end_year + 1):

        if is_leap_year(year):
            print(year)

test_is_leap_year(1996,2112)
