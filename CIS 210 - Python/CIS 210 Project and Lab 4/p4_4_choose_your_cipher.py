# CIS 210 Winter 2021-2022 Project 4
# Karma Woeser
# Project 4 - Choose your cipher


from p4_1 import encrypt, decrypt
from p4_2 import encrypt, decrypt
from p4_3 import encrypt, decrypt

'''
def crypt(msg: str) -> str:
    return p4_1.encrypt(msg)
    return p4_2.encrypt(msg)
    return p4_3.encrypt(msg)
'''


def crypt(msg, func):
    if func == p4_1.encrypt:
        return p4_1.encrypt(msg)


#print(crypt('Ahoy There!', p4_1.encrypt))
    
