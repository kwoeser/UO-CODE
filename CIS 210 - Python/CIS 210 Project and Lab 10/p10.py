"""
Project 10 solution
Author: Karma Woeser
Date: 3-7-2022
"""

def count_smaller(lst: list, item: int) -> int:
    '''Looks through a list for the amount of integers smaller the the item integer using recursion
    Args:
        lst: the list that will be looked through
        item: anything number less then the item will be printed
    Returns:
        The number of ints smaller then the item int
        
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    4

    >>> count_smaller([], 5)
    0
    '''
    if lst == []:
        return 0
    else:
        if item > lst[0]:
            return 1 + count_smaller(lst[1:], item)
        else:
            return count_smaller(lst[1:], item)
        

def is_palindrome(s: str) -> bool:
    '''Checks if the string is a palindrome using recursion 
    Args:
        s: the string that will be checked if it's a palindrome
    Returns:
        True if the string is a palindrome and false if it is not

    >>> is_palindrome('racecar') 
    True
    
    >>> is_palindrome('racecars') 
    False 
    '''

    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False




def avg_word_length(lst:list, length:int=0, count:int=0)->float:
    '''finds the avergage word length of a list of words using recursion
    Args:
        lst: the list of words 
        length: the amount of words in list
        count: the count of letters
    Returns:
        the average word length from the list (float)

    >>> avg_word_length(['hello', 'world']) 
    5.0
    
    >>> avg_word_length(['hello', 'world', 'meh']) 
    4.3 
    '''

    if lst == []:
        return round(float(length/count), 1)
    else:
        count += 1
        length += len(lst[0])
        return avg_word_length(lst[1:], length, count)
            

def flatten(a_list:list) -> list:
    '''flattens a sorted list using recursion
    Args:
        a_list: the list that will be flattened
    Returns:
        the flatten list
        
    >>> flatten([1, 2, 3])
    [1, 2, 3]

    >>> flatten([1, [2, [3, 4, [5], 6], 7], 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    
    if a_list == []:
        return a_list
    elif isinstance(a_list[0], list):
        return flatten(a_list[0]) + flatten(a_list[1:])
    else:
        return a_list[:1] + flatten(a_list[1:])
        

