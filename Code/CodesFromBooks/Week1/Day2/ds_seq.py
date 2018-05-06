shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
counter=0
for i in shoplist:
    print('Item {} is {}'.format(counter,i))
    counter+=1

print(shoplist)
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Character 0 is',name[0])

print('From 0-3',shoplist[0:3])
print('Item from 2:end',shoplist[2:])
print('From start to end',shoplist[:])