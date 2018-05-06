while True:
    s=input("Enter something:")

    if s=='quit':
        break
    elif len(s)<3:
        print("Too small")
    else:
        print(s)
print("Done")