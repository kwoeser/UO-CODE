# CIS 210 Winter 2021-2022 Project 4
# Karma Woeser
# Project 4 - ROT13 Cipher

def encrypt(msg:str) -> str:
    '''
    Encrypts the messgae using the ROT13 cipher

    Args:
        msg: the messge that will be encryped

    Returns:
        cipherText: the encryped message

    >>> encrypt('karma')
    'xnezn'

    >>> encrypt('cipher')
    'pvcure'
    '''
    abcs = 'abcdefghijklmnopqrstuvwxyz'
    key = 13
    msg = msg.lower()
    cipherText = ''
    
    for char in msg:
        messageN = (abcs.find(char) + key) % len(abcs)
        if char in abcs:
            cipherText += abcs[messageN]
        else:
            cipherText += ' '

    return cipherText


def decrypt(msg:str) -> str:
    '''
    Decrypts the ROT13 cipher

    Args:
        msg: the message that will be decryped

    Returns:
        plainText: the decrypted message

    >>> decrypt('xnezn')
    'karma'

    >>> decrypt('pvcure')
    'cipher'
    '''
    abcs = 'abcdefghijklmnopqrstuvwxyz'
    key = 13
    msg = msg.lower()
    plainText = ''
    
    for char in msg:
        messageN = (abcs.find(char) - key) % len(abcs)
        if char in abcs:
            plainText += abcs[messageN]
        else:
            plainText += ' '

    return plainText
