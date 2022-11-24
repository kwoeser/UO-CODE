# CIS 210 Winter 2021-2022 Lab 5
# Karma Woeser
# Lab 5 - odd-even cipher

'''
0          0
01        10
012      102
0123    1302

'''
def encrypt(msg:str) -> str:
    evens = ''
    odds= ''
    for char_index in range(0, len(msg) -1, 2):
        evens += msg[char_index]
        odds += msg[char_index + 1]

    return odds + evens




def decrypt(msg:str) -> str:
    msg_len = len(msg)
    middle = msg_len // 2
    decrypted = ''
    for i in range(middle):
        decrypted += msg[middle + i] + msg[i]

    return decrypted


def main():

    which = input('Do you wish to encrypt or decrypt the message [E/D]?')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print('Encrypted text:')
        print(encrypt(text))

    elif which.upper() == 'D':
        text = input('Enter a line of text to decrpyt: ')
        print('Decryped text:')
        print(decrypt(text))

    else:
        raise ValueError('Invalid Option, I only know E and D!')
    

if __name__ == '__main__':
    main()


