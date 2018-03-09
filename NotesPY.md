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
#prints from 0 to 4(if added 3rd number in brackets(0,5,X) prints every i+X)
```
Data types
```py
#IF *LIST THEN I CAN PUT sep="." ect. for separating with . not with spaces
#LIST
list=["item1","item2","item3"]
#printing it
print(list)

#TUPLES
#Same like list but without extensive funcionality  (they are immutable also)
tuple=("Car",1,0,5)
print(tuple)
#>> car 1 0.5


#DICTIONARY
ab={
'Key1':'Item1',
'Key2':'Item2'
}
#printing
print(ab['Key1'])#prints Item1

#printing list element as in dict parametar valute()
names={"imena":["karlo","pero","duro"],"prezimena":["kegljevic","peric","duric"]}
 for i in range(3):
    print("IME:",names['imena'][i])
    print("PREZIME:",names['prezimena'][i])

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
#CONVERTING LIST TO STRING
some_list=["k","a","r","l","o"]
names=''.join(some_list)

# default spaces in rjust ljust in second parametar 
'hello'.rjust(10,'*')
#prints '*****hello'

'hello'.ljust(10,'*')
#prints 'hello*****'

'hello'.center(10,'=')
#prints '==hello==='


name = 'Swaroop'

if name.startswith('Swa'):
  print('Yes, the string starts with "Swa"')
'hello'.isalpha()   #returns True if the string consists only of letters and is not blank
'hello'.isalnum()   #returns True if the string consists only of letters and numbers and is not blank
'hello'.isdecimal() #returns True if the string consists only of numeric characters and is not blank
'hello'.isspace()   #returns True if the string consists only of spaces, tabs, and newlines and is not blank
'hello'.istitle()   #returns True that begin with an uppercase letter followed by only lowercase letters.

if 'a' in name:
  print('Yes , it contains "a"')
if name.find('war')!= -1:
  print('Yes it conaints the string "war"')

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))#prints mylist[0] delimiter then mylist[1] ..
```

Regex
```py
import re
#\d stands for a digit character(0-9)
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#makes search "term"
mo= phoneNumRegex.search('My number is 123-123-1234')#searches for "term" in string, and puts it in mo if it finds it
print('Phone number found: ' + mo.group())#mo.group() prints finded "term"
#you can also group items in phoneNumRegex-> phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#and then you can use mo.group(1) to print first group of phoneNumRegex(3digits) .group(0) prints all ,
# .groups() returns tuple of groups (3digits,3digs-4digs)
# you can add names to grouped parametars ( first,second = mo.groups()) first will be 3digs , 
# second will be 3digs-4digs

#OPTIONAL MATCHING WITH ? MARK
batRegex = re.compile(r'Bat(wo)?man')
mo1= batRegex.search('The adventures of Batman')
mo1.group()
# 'Batman'
mo2=batRegex.search('The adventure of Batwoman')
mo2.group()
# 'Batwoman'
```











