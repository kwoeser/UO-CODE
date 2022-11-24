"""
Lab 10 solution
Author: Karma Woeser
Date: 3-8-2022
"""

'''
1 is the base case
n! = n * (n-1) * (n-2) * (n-3) ... * 1

this is the recursive case
n! = n * (n-1)!

5! = 5 * 4
5! = 5 * 4!


def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n-1)

print(factorial_recursive(0))
'''

def get_vowel_count(s: str)-> int:
    """Counts the numbe of vowels in the str
    Args:
        s: the string whose vowels will be counted
    Returns:
        The number of vowels in s (the string)

    >>> get_vowel_count('jeager')
    3

    >>> get_vowel_count('qwsd')
    0
    """
    # base case
    if s == '':
        return 0
    
    else:
        if s[0] in 'aieou':
            return 1 + get_vowel_count(s[1:])
        else:
            return get_vowel_count(s[1:])



def multiply(a: float, b: int) -> float:
    """Multiples a float with an integer and outputs a float
    Args:
        a: the float that will be multipled
        b: the int that will be multipled
    Returns:
        The float sum of a and b

    >>> multiply(5.0, 4)
    20

    >>> multiply(10.0, 9)
    9
    """
    if b == 0:
        return 0
    else:
         return a + multiply(a, b-1)

    


'''
[1, [2, 3], 4]
[1, [3, 2], 4]
[4, [3, 2], 1]
'''
def deep_reverse(a: list) -> list:
    """Reverse the list and the list inside 
    Args:
        a: the list that will be being deep reversed
    Returns:
        The deep reversed list

    >>> deep_reverse([1, [2, 3], 4])
    [4, [3, 2], 1]

    >>> deep_reverse([1, [2, [3, 4], [5, [6, 7], 8]]])
    [[[8, [7, 6], 5], [4, 3], 2], 1]
    
    """
    if a == []:
        return a
    elif isinstance(a[0], list):
        return deep_reverse(a[1:]) + [deep_reverse(a[0])]
        
    else:
        return deep_reverse(a[1:]) + [a[0]]


    
