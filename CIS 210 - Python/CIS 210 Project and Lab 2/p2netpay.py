# CIS 210 Winter 2021-2022 Project 2
# Karma Woeser
# Project 2 - Netpay


'''
Module p2netpay.py

Functions:
        tax(gross_pay)
        netpay(hours_worked)
        main()
'''

def tax(gross_pay):
    '''
    Explaination: Mulplities the total gross_pay with the tax rate which gives us the total
    amount of tax. (tax_amount)

    Parameters: gross_pay (int)

    Returns: the amount of the tax (tax_amount)
    '''
    # 15%
    tax_rate = 15/100
    tax_amount = gross_pay * tax_rate
    return tax_amount




def netpay(hours_worked):
    '''
    Explaination: Takes the hours_worked and multiplies it by the hourly rate of $16.25
    which is the total gross pay (gpay).
    Then takes that gross pay and subtracts it by the total amount of tax which is the
    netpay amount (npay)

    Parameters: hours_worked (int)

    Returns: netpay (npay)
    '''
    gpay = hours_worked * 16.25
    npay = gpay - tax(gpay)

    return npay



def main(): 
    '''Net pay program driver.''' 
    print('For 1 hour of work, netpay is:', round(netpay(1), 2))  
    print('For 40 hours of work, netpay is:', netpay(40)) 
    return None

 
main()  
    
