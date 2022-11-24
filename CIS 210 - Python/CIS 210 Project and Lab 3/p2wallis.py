# CIS 210 Winter 2021-2022 Project 3
# Karma Woeser
# Project 3 - Wallis Method


def pi_wallis(num_pairs: int) -> float:
    '''
    Explaination: Finds the approxmation of pi using the Wallis method

    Parameters: num_pairs: the number of pairs

    Returns: pi

    >>> pi_wallis(100)
    3.1337874906281575

    >>> pi_wallis(1)
    2.6666666666666665
    '''
    acc = 1
    num = 2

    for aPair in range(num_pairs):
        leftTerm = num / (num - 1)
        rightTerm = num / (num + 1)

        acc = acc * leftTerm * rightTerm

        num += 2

    pi = acc * 2
    return pi
