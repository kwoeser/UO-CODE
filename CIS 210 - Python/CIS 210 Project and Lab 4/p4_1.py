# CIS 210 Winter 2021-2022 Project 4
# Karma Woeser
# Project 4 - Simple Transposition Cipher

def encrypt(msg:str) -> str:
    '''
    Encrypts a message using an odd-even transposition cipher

    Args:
        msg: the message that is going to be encrypted

    Returns:
        cipherText: the encrypted message
    '''
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in msg:            
        if charCount % 2 == 0:          
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def decrypt(msg:str) -> str:
    '''
    Decrpyts an encrypted cipher

    Args:
        msg: the message that is going to be decryped

    Returns:
        plainText: the decrypted message
    '''
    halfLength = len(msg) // 2
    oddChars = msg[:halfLength]
    evenChars = msg[halfLength:]     
    plainText = ""
    
    for i in range(halfLength):             
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
        
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]
        
    return plainText



        


