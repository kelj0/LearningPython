import random

def one():
    a="""
    ***********
    *         *
    *    O    *
    *         *
    ***********
    """
    return a
def two():
    a="""
    ***********
    *    O    *
    *         *
    *    O    *
    ***********
    """
    return a
def three():
    a="""
    ***********
    *    O    *
    *    O    *
    *    O    *
    ***********
    """
    return a
def four():
    a="""
    ***********
    *  O   O  *
    *         *
    *  O   O  *
    ***********
    """
    return a
def five():
    a="""
    ***********
    *  O   O  *
    *    O    *
    *  O   O  *
    ***********
    """
    return a
def six():
    a="""
    ***********
    *  O   O  *
    *  O   O  *
    *  O   O  *
    ***********
    """
    return a


more='y'
while more=='y':
    dice=random.randint(1,6)
    if dice==1:
        print(one())
    elif dice==2:
        print(two())
    elif dice==3:
        print(three())
    elif dice==4:
        print(four())
    elif dice==5:
        print(five())
    elif dice==6:
        print(six())

    more=input('\n1 more roll?[y]es/[n]o:')
