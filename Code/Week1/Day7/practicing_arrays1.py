def printing(spam):
    for i in range (0,len(spam)):
        if i==(len(spam)-1):
            print("and",spam[i])
        else:
            i=int(i)
            print(spam[i],end=", ")

spam=['apples','bananas','tofu','cats']
printing(spam)