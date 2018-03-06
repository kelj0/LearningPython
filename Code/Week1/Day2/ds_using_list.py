shopinglist =['bread','apple','mango']
print('I have', len(shopinglist))

print('This are the items:',end=' ')
for item in shopinglist:
    print(item,end=' ')

print('\nI also have to buy rice.')
shopinglist.append('rice')
print('My shopping list is now',shopinglist)

print('I will sort items now')
shopinglist.sort()
print('Sorted shoping list is', shopinglist)

print('The first item i will buy is',shopinglist[0])
olditem=shopinglist[0]
del shopinglist[0]
print('I bought the',olditem)
print('First item now is',shopinglist[0])
print('My shoping list is now',shopinglist)
