def maximum(x,y):
    if x>y:
        return "X is bigger({})".format(x)
    elif x<y:
        return "Y is bigger({})".format(y)
    else:
        return "They are same"
print(maximum(1,2))
print(maximum(10,4))
print(maximum(1,1))