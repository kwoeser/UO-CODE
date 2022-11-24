# CIS 210 Winter 2021-2022 Lab 4
# Karma Woeser
# Lab 4 

def hello(firstname): 
    ''' 
    prints the hello and the firstname

    Args:
        firstname: the firstname

    Returns:
        None
    ''' 
    print("Hello, "+firstname+"!") 
    return None 

 
def ciao(firstname): 
    ''' 
    prints Ciao and the firstname

    Args:
        firstname: the firstname

    Returns:
        None
    ''' 
    print("Ciao, "+firstname+"!") 
    return None 


def greeting(f, s):
    '''
    Calls a function and prints the name of the function

    Args:
        f: the function that is being called
        s: string

    Returns:
        None

    '''
    print('Calling', f.__name__)
    f(s)
    return None

#greeting(hello, 'orange!')
#greeting(ciao, 'kiwi')


def add_3(a,b,c):
    '''
    Takes three numbers and adds them together

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        abc: the sum of the three numbers
    '''
    abc = a + b + c
    return abc


def multi_3(a,b,c):
    '''
    Takes three numbers and multiplies them together

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        abc: the sum of the three numbers
    '''
    abc = a * b * c
    return abc


def higher_order(f, a,b,c):
    '''
    Calls a function then takes three numbers and adds them or multiplies them depending
    on your input

    Args:
        f: the function that is being called
        a: first number
        b: second number
        c: third number

    Returns:
        value: the function that is being used to find the sum of the three numbers
    '''
    print('Function:', f.__name__)
    value = f(a,b,c)
    print(f.__name__, '(', a, ',', b, ',', c, ')', '=', value)
    return value

higher_order(add_3, 1, 2, 3)
higher_order(multi_3, 10, 20, 30)
