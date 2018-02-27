# PYTHON


Printing text
```py
print("Print text")
```
Operators(no 2 times like in cpp &&->&)

While
```py
while True:
  s=input("Enter string")
  if s=='quit':
    break
  else:
  print(s)
```

For
```py
for i in range(0,5):
  print(i)
#prints from 0 to 4(if added 3th number in brackets(0,5,X) prints every i+X)
```
Data types
```py
#LIST
list=["item1","item2","item3"]
#printing it
print(list);print(list(:)
#TUPLES
#Same like list but without extensive funcionality  (they are immutable also)

#DICTIONARY
ab={
'Key1':'Item1',
'Key2':'Item2'
}
#printing
print(ab['Key1'])#prints Item1

#SEQUENCES
#same ase list but with aditional foo
#first parameter is where to begin(if not it begins from start)
#second parametar is where to end(if not it ends on end)
#third parametar is jump ( if 2 then 1,3 from seq[1,2,3,4]
print("List from 0-2",shopinglist[0:3])
print("List all",shopinglist[:]
print("List by i+=X",shopinglist[::X]
#lists all seq but every X item
```
Strings
```py
name = 'Swaroop'

if name.startswith('Swa'):
  print('Yes, the string starts with "Swa"')
if 'a' in name:
  print('Yes , it contains "a"')
if name.find('war')!= -1:
  print('Yes it conaints the string "war"')

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))#prints mylist[0] delimiter then mylist[1] ..

