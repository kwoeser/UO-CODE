# CIS 210 Winter 2021 Project 1
# Karma Woeser
# Project 1 - Builtin types
# References: https://mathbitsnotebook.com/Algebra1/RealNumbers/RNProp.html

# Distributive Property
def one(a,b,c):
    '''Should print false'''
    print(a*(b+c) == a*b + a*c)

one(10, 0.1, 0.2)

# Associative Property of Addition
def two(a,b,c,):
    '''I believe the APOA will print a false statement
    Prints true when different numbers are entered'''
    print(a + (b + c) == (a + b) + c)

two(10, 1.2, 0.00001)

# Associative Property of Multiplication
def three (a, b, c):
    '''Think it will print false'''
    print(a * (b * c) == (a * b) * c)

three(10, 0.1, 0.2)


# Transitive Property of Equality
def four(a, b, c):
    '''I think this one might print True because a and c should be equal to each other

    Since a = b and b = c. Then a should equal c.'''
    a = b
    b = c
    print(a/b/c == c/b/a)


four(0.002, 10, 5)

# Commutative Property
def five(a, b, c):
    ''' I thought it would print true 

    Even tho the equation equals 0.004 when you do it on paper. It's not 0.004 for this
    equation. It comes out to around 0.3999. 
    '''
    print(a + b - c  == 0.004)
    
five(5, 1.004, 6)





