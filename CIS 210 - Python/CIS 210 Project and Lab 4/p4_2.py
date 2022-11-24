# CIS 210 Winter 2021-2022 Project 4
# Karma Woeser
# Project 4 - Three Rail Cipher

def encrypt(msg:str) -> str:
    '''
    Encrypts a message using the Three Rail cipher

    Args:
        msg: the message that is going to be encrypted

    Returns:
        cipherText: the encrypted message

    >>> encrypt('karma')
    'kmaar'

    >>> encrypt('rail')
    'rlai'
    '''
    firstRow = ''
    secondRow = ''
    thirdRow = ''
    count = 0

    for i in range(len(msg)):
        if i % 3 == 0:
            firstRow += msg[i]
    
        elif i % 3 == 1:
            secondRow += msg[i]

        elif i % 3 == 2:
            thirdRow += msg[i]

        
    cipherText = firstRow + secondRow + thirdRow
    return cipherText


        
def decrypt(msg:str) -> str:
    '''
    Decrypts the three rail ciphered message

    Args:
        msg: the message that is going to be decryped

    Returns:
        plainText: the decrypted message
    '''
    firstRow = ''
    secondRow = ''
    thirdRow = ''
    count = 0

    for i in range(len(msg)):
        if i % 3 == 0:
            firstRow += msg[i]
    
        elif i % 3 == 1:
            secondRow += msg[i]

        elif i % 3 == 2:
            thirdRow += msg[i]

        
    plainText = firstRow + secondRow + thirdRow
    return plainText
    
