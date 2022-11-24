# CIS 122 Fall 2020 Assignemnt 4 v2
# Author: Karma Woeser
# Partner: Your Partner
# References:
# Description: Yearday v2

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

#print(is_leap_year(2020))
#print(is_leap_year(2021))


def valid_year(year):
    if year > 0:
        return True
    else:
        print("Year must be > 0")
        return False

#print(valid_year(0))
#print(valid_year(2020))

    
def valid_day_of_year(year, day_of_year):
    if day_of_year > 0:
        return True
    else:
        print("Day of year must be > 0")
        return False

#print(valid_day_of_year(2020, 0 ))
#print(valid_day_of_year(2020, 31))


def input_year():
    year = int(input("Enter Year: "))
    if year <= 0:
        year = int(input("Enter Year: "))
        print("Day of year must be > 0")
    if valid_year(year) is True:
        return year

#input_year(2020)


def get_days_in_year(year):
    if is_leap_year(year) is True:
        return 366
    if is_leap_year(year) is False:
        return 365
    else:
        return 0

#print(get_days_in_year(2020))
#print(get_days_in_year(2021))


def input_days_in_year(year):
    day = int(input("Enter the day of year: "))
    if is_leap_year(year) is True:
        if day > get_days_in_year(year) or day <= 0:
            if day > get_days_in_year(year):
                print("Day must be <= 366")
                day = int(input("Enter Day of year: "))
            if day <= 0:
                print("Day must be > 0")
                day = int(input("Enter Day of year: "))
        if valid_year(year) and valid_day_of_year(year, day):
                return day
    elif is_leap_year(year) is False:
        if day > get_days_in_year(year) or day <= 0:
            if day > get_days_in_year(year) or day <=0 :
                print("Day must be <= 366")
                day = int(input("Enter Day of year: "))
        if valid_year(year) and valid_day_of_year(year, day):
            return day
        else:
            return 0

#print(input_day_of_year(21))


def valid_month(month):
    if month > 0 and 0 <= 12:
        return True
    elif month <= 0:
        print("Month must be > 0")
        return False
    elif month >= 12:
        print("Month must be <= 12")
        return False

#print(valid_month(1))
#print(valid_month(0))


def translate_month(month):

    if valid_month(month):
        if month == 1:
            return "January"
        elif month == 2:
            return "Feburay"
        elif month == 3:
            return  "March"
        elif month == 4:
            return "April"
        elif month == 5:
            return "May"
        elif month == 6:
            return "June"
        elif month == 7:
            return "July"
        elif monthr == 8:
            return "August"
        elif month == 9:
            return "September"
        elif month == 10:
            return "October"
        elif month == 11:
            return "November"
        elif month == 12:
            return "December"
        else:
            print("You must enter an integer between 1 and 12.")


#print(translate_month(5))
#print(translate_month(0))


def get_days_in_month(year,month):
    ''' Purpose: 
    
    '''
    if month == 1:
        return 31
    elif is_leap_year(year) is True and valid_month(month) is True and month == 2:
        return 29
    elif is_leap_year(year) is False and valid_month(month) is True and month == 2:
        return  28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif monthr == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return 0

#print(get_days_in_month(0, 0))
#print(get_days_in_month(2020, 5))

def valid_day(year, month, day):
    if valid_day(year) is True and valid_month(month) is True and valid_day_of_year(year, day) is True:
        return True
    else:
        return False

#print(valid_day(2020, 0, 0))
#print(valid_day(2020, 1, 21))


def get_date_string(year, month, day):
    if is_leap_year(year) is True and valid_year(year) is True:
        if day == 1 or day <= 31:
            month = "January"
        elif day == 32 or day <= 60:
            month = "Feburay"
            day -= 31
        elif day == 61 or day <= 91:
            month = "March"
            day -= 60
        elif day == 92 or day <= 121:
            month = "April"
            day -= 91
        elif day == 122 or day <= 152:
            month = "May"
            day -= 121
        elif day == 153 or day <= 182:
            month = "June"
            day -= 152
        elif day == 183 or day <= 213:
            month = "July"
            day -= 182
        elif day == 214 or day <= 244:
            month = "August"
            day -= 213
        elif day == 245 or day <= 274:
            month = "September"
            day -= 244
        elif day == 275 or day <= 305:
            month = "October"
            day -= 274
        elif day == 306 or day <= 335:
            month = "November"
            day -= 305
        elif day == 336 or day <= 366:
            month = "December"
            day -= 335
        else:
            return ""
        print(str(month), str(day), ',', str(year))
    if is_leap_year(year) is False and valid_year(year) is True:
        if day == 1 or day <= 31:
            month = "January"
        elif day == 32 or day <= 59:
            month = "Feburay"
            day -= 31
        elif day == 60 or day <= 90:
            month = "March"
            day -= 59
        elif day == 91 or day <= 120:
            month = "April"
            day -= 90
        elif day == 121 or day <= 151:
            month = "May"
            day -= 120
        elif day == 152 or day <= 181:
            month = "June"
            day -= 151
        elif day == 182 or day <= 212:
            month = "July"
            day -= 181
        elif day == 213 or day <= 243:
            month = "August"
            day -= 212
        elif day == 244 or day <= 273:
            month = "September"
            day -= 243
        elif day == 275 or day <= 305:
            month = "October"
            day -= 274
        elif day == 305 or day <= 334:
            month = "November"
            day -= 304
        elif day == 335 or day <= 365:
            month = "December"
            day -= 334
        print(str(month), str(day), ", ", str(year))
    else:
        return ""

#print(get_date_string(2020,1,21))
#print(get_date_string(2021,1,21))
#print(get_date_string(0, 0, 0))

def start():

    year = input_year()
    month = get_date_string
    day = input_days_in_year(year)
    return get_date_string(year, month, day)

print(start())
