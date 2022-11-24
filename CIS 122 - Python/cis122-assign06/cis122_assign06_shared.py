# CIS 122 Fall 2021 Assignment 6
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: shared problem

def pad_string(data, size, direction = 'left' , character = ''):
    '''Purpose: To create padding on string

    Arguments: data: The data that will have the padding
    size: The size of the padding; how far from the left you want to move the data
    direction: asking which direction the padding will be placed; default is left
    character: Character/s that will be padded

    Returns: right_padding which will be the amount of space(padding) that will be applied
    '''
    if len(data) > size:
        return str(data)
    
    elif direction == 'left':
        return pad_left(str(data), size, character)
    else:
        return pad_right(str(data), size, character) 

    
def pad_left(data, size, character = ''):
    '''Purpose: To create a padding to the left

    Arguments: data: The data that will have the padding
    size: The size of the padding; how far from the left you want to move the data
    character: Character/s that will be padded

    Returns: left_padding which will be the amount of space(padding) that will be applied
    '''
    left_padding = character * size + str(data)
    return left_padding


def pad_right(data, size, character = ''):
    '''Purpose: To create a padding to the left

    Arguments: data: The data that will have the padding
    size: The size of the padding; how far from the left you want to move the data
    character: Character/s that will be padded

    Returns: right_padding which will be the amount of space(padding) that will be applied
    '''
    right_padding = character * size + str(data[::- 1])
    return right_padding


