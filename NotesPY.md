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
names={"imena":["karlo","pero","duro"],"prezimena":["kegljo","peric","duric"]}
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

Working with files
```py
import os
os.getcwd() #Current working directory in string format
os.chdir("C:\\Windows\\System32") #Changes working dir
os.makedirs("C:\\delicious\\walnut\\waffles") #Makes dir delicious folder ,then inside delicious walnut,(*)
os.path.abspath(path) #returns string of apsolute path                    *(then inside walnut waffles folder)            
os.path.isabs(path) #Returns True if is absolute
os.path.relpath(path,start) #Will return string of a path from start to path
os.path.exists(path) # returns True if refered file in path exists
os.path.isfile(path) #returns True if path argument exists and is file
os.path.isdir(path)  #returns True if path argument exists and is folder

#R/W FILES
#1. open()
#2. read() or write() 
#3. close()

baconFile=open('bacon.txt','w') #second argument in open is 'w'(overwrites file with new contet)
baconFile.write('Hello world!\n') #it returns num of chars written including newline
#dont forget to close file after writing/reading to it
baconFile.close()

baconFile=open('bacon.txt','a') #second arg is 'a' unlike 'w'  it appends contet
baconFile.write('Bacon is not a vegetable.')
#dont forget to close 
baconFile.close()

baconFile.open('bacon.txt')
contet=baconFile.read()
baconFile.close()
print(conte)
#prints contet of baconFile(Hello world!\nBacon is not a vegetable)


```

Regex
```py
import re
#\d stands for a digit character(0-9)
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#makes search "term"
mo= phoneNumRegex.search('My number is 123-123-1234')#searches for "term" in string, and puts it* 
print('Phone number found: ' + mo.group())#mo.group() prints finded "term"             *in mo if it finds it
#you can also group items in phoneNumRegex-> phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#and then you can use mo.group(1) to print first group of phoneNumRegex(3digits) .group(0) prints all ,
# .groups() returns tuple of groups (3digits,3digs-4digs)
# you can add names to grouped parametars ( first,second = mo.groups()) first will be 3digs , 
# second will be 3digs-4digs


batRegex = re.compile(r'Bat(wo)?man')
mo1= batRegex.search('The adventures of Batman')
mo1.group()
# 'Batman'

mo2=batRegex.search('The adventure of Batwoman')
mo2.group()
# 'Batwoman'

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
# 'Batwowowowoman'


batRegex = re.compile(r'Bat(wo)+man')
mo4 = batRegex.search('The Adventures of Batman')
mo4 == None
# True

#SHORTHAND CODES FOR COMMON CHARACTER CLASSES
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character.(Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S Any character that is not a space, tab, or newline.

#NEGATIVE CHAR CLASS
constantRegex = re.compile(r'[^aeiouAEIOU])
constantRegex.findall("Robocop eats baby food.BabyFood.")
#it will output all chars that are != from constantRegex

#also you can use it to find first(^) or last match($)
beginingHello=re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
beginingHello.search('He said hello.') == None
#True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
#<_sre.SRE_Match object; span=(16, 17), match='2'>


#Findin all chars exept newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']

```
