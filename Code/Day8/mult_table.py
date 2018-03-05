for i in range(11):
    for j in range(11):
        if (i*j)>=10:
            print(str(i*j)+"|",end="")
        else:
            print(str(i*j)+" |",end="")
    print()