# CIS 210 Winter 2021-2022 Project 5
# Karma Woeser
# Project 5 - Postfix


stack = []

operator_lst = ['+', '-', '*', '/']

def is_operand(operand:str)->bool:
    abcs = 'qwertyuiopasdfghjklzxcvbnm'
    symbols = '-=`,./;{}+|!@#$%^&*()_+<>?:"{}|,./;`~[]'

    for i in abcs:
        if operand == i:
            return False
    for s in symbols:
        if operand == s:
            return False
        elif operand == int or float:
            return False
        else:
            stack.append(operand)
            return True
            

   

def is_operator(operator:str)->bool:

   
    for oper in operator_lst:
        if operator == oper:
            stack.pop(-1)
            return True
        else:
            return False



def apply_operator(op:str, oper_1:float, oper_2:float)->float:

    for oper in operator_list:
        if op == oper:
            
    
    return op

apply_operator('*', 3, 4)

def eval_postfix(expr_str:str)->float:
    return expr_str
