#!/usr/bin/python3
x=20
print ("x before function is",x)
def change_x(x):
    x=2
    print("X in function is {}".format(x))

change_x(x)
print("x outside funcion is" ,x)