x=10

def change_x():
    global x

    print("Changing X in funciont..x is ", x)
    x=2
    print ("After change X is.. ",x)
change_x()
print("After funcion in main x is ",x)