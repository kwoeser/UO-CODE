# CIS 210 Winter 2021 Lab 2
# Karma Woeser
# Lab 2 is_even 


def is_even(n: int) -> bool:
    print('in function is_even')

    """ Determines if n is an even number. 
 
    Args: 
        n: an integer number 
 
    Returns: 
        True if n is an even number, False otherwise 
 
    >>> is_even(100) 
    True 
    >>> is_even(101) 
    False 
    >>> is_even(0) 
    True 
    """ 
 
    return (n % 2) == 0 


#is_even(2) 
#result = is_even(3)
is_even(3)
print(is_even(3))
is_even(2.0)



def welcome(): 
   """Print a welcome message.  
   >>> welcome() 
   Good morning, CIS 210! 
   """ 
   print('Good morning, CIS 210!') 
   return None 
  
welcome()

