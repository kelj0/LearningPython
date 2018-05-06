def func(a,b=2,c=3):
    print("a is {} , b is {}, c is {}".format(a,b,c))

a=10
b=20
c=30
func(a,b)
func(a,c=50,b=100)